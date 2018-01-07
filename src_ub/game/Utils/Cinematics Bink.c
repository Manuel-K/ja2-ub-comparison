#include "Types.h"
#include <stdio.h>
#include <io.h>
#include <string.h>
#include <fcntl.h>
#include <share.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <malloc.h>
#include <stdlib.h>

#include "DEBUG.H"
#include "FileMan.h"
#include "smack.h"
#include "ddraw.h"
#include "mss.h"
#include "DirectX Common.h"
#include "DirectDraw Calls.h"
#include "soundman.h"
#include "video.h"

#include "Cinematics Bink.h"

#include "vsurface_private.h"

//#include "Intro.h"


#include "radmalw.i"


#include <crtdbg.h>



//*******************************************************************
//
// Local Defines
//
//*******************************************************************


#define BINK_NUM_FLICS							4										// Maximum number of flics open



//*******************************************************************
//
// Global Variables
//
//*******************************************************************

BINKFLIC BinkList[BINK_NUM_FLICS];					
UINT32	 guiBinkPixelFormat=0;

//LPDIRECTDRAWSURFACE lpBinkVideoPlayback=NULL;
LPDIRECTDRAWSURFACE2 lpBinkVideoPlayback2=NULL;
HWND				hBinkDisplayWindow=0;
UINT32			guiHeight;



//*******************************************************************
//
// Function Prototypes
//
//*******************************************************************

void				BinkInitialize(HWND hWindow, UINT32 uiWidth, UINT32 uiHeight);
void				BinkShutdown(void);
BINKFLIC		*BinkPlayFlic(CHAR8 *cFilename, UINT32 uiLeft, UINT32 uiTop, UINT32 uiFlags );
BOOLEAN			BinkPollFlics(void);
BINKFLIC		*BinkOpenFlic(CHAR8 *cFilename);
void				BinkSetBlitPosition(BINKFLIC *pBink, UINT32 uiLeft, UINT32 uiTop);
void				BinkCloseFlic(BINKFLIC *pBink);
BINKFLIC		*BinkGetFreeFlic(void);
void				BinkSetupVideo(void);
void				BinkShutdownVideo(void);
UINT16			GetNumberOfBits( UINT32 uiMask );





//*******************************************************************
//
// Functions
//
//*******************************************************************



void				BinkInitialize(HWND hWindow, UINT32 uiWidth, UINT32 uiHeight)
{
	HDIGDRIVER pSoundDriver = NULL;


	//Get the sound Driver handle
	pSoundDriver = SoundGetDriverHandle();

	//if we got the sound handle, use sound during the intro
	if( pSoundDriver )
	{
		BinkSoundUseMiles( pSoundDriver );
	}

	guiHeight = uiHeight;
}


void				BinkShutdown(void)
{
	UINT32 uiCount;

	// Close and deallocate any open flics
	for(uiCount=0; uiCount < BINK_NUM_FLICS; uiCount++)
	{
		//if the flic is currently open
		if(BinkList[uiCount].uiFlags & BINK_FLIC_OPEN )
		{
			//close it
			BinkCloseFlic( &BinkList[uiCount] );
		}
	}
}



BINKFLIC			*BinkPlayFlic(CHAR8 *cFilename, UINT32 uiLeft, UINT32 uiTop, UINT32 uiFlags )
{
	BINKFLIC *pBink;

	// Open the flic
	if( ( pBink = BinkOpenFlic( cFilename ) ) == NULL )
	{
		return(NULL);
	}

	if( uiFlags & BINK_FLIC_CENTER_VERTICAL)
	{
		uiTop = ( guiHeight - pBink->BinkHandle->Height ) / 2;
	}

	// Set the blitting position on the screen
	BinkSetBlitPosition( pBink, uiLeft, uiTop);

	// We're now playing, flag the flic for the poller to update
	pBink->uiFlags |= BINK_FLIC_PLAYING;

	if( uiFlags & BINK_FLIC_AUTOCLOSE )
	{
		pBink->uiFlags |= BINK_FLIC_AUTOCLOSE;
	}
	else
	{
		pBink->uiFlags |= BINK_FLIC_LOOP;
	}


	return(pBink);
}

BINKFLIC *BinkOpenFlic( CHAR8 *cFilename )
{
	BINKFLIC *pBink;
	HANDLE	hFile;

	// Get an available flic slot from the list
	if( !( pBink = BinkGetFreeFlic() ) )
	{
		ErrorMsg("BINK ERROR: Out of flic slots, cannot open another");
		return(NULL);
	}

	// Attempt opening the filename
	if(!(pBink->hFileHandle = FileOpen( cFilename, FILE_OPEN_EXISTING | FILE_ACCESS_READ, FALSE ) ) )
	{
		ErrorMsg("BINK ERROR: Can't open the BINK file");
		return(NULL);
	}

	//Get the real file handle for the file man handle for the smacker file
	hFile = GetRealFileHandleFromFileManFileHandle( pBink->hFileHandle );

	if( !( pBink->BinkHandle = BinkOpen((CHAR8 *)hFile, BINKFILEHANDLE ) ) ) //| SMACKTRACKS 
	{
		ErrorMsg("BINK ERROR: Bink won't open the BINK file");
		return(NULL);
	}

	// Make sure we have a video surface
	BinkSetupVideo();

	pBink->cFilename = cFilename;

	pBink->lpDDS = lpBinkVideoPlayback2;

	pBink->hWindow = hBinkDisplayWindow;

	// Bink flic is now open and ready to go
	pBink->uiFlags |= BINK_FLIC_OPEN;

	return( pBink );
}



BINKFLIC *BinkGetFreeFlic()
{
	UINT32 uiCount;

	//loop through to get a free slot
	for( uiCount=0; uiCount < BINK_NUM_FLICS; uiCount++ )
	{
		//if this slot is currently not in use
		if( !( BinkList[uiCount].uiFlags & BINK_FLIC_OPEN ) )
		{
			return( &BinkList[ uiCount ] );
		}
	}

	return( NULL );
}


void BinkSetBlitPosition( BINKFLIC *pBink, UINT32 uiLeft, UINT32 uiTop )
{
	pBink->uiLeft = uiLeft;
	pBink->uiTop = uiTop;
}
	
void BinkCloseFlic( BINKFLIC *pBink )
{
	// Deallocate the smack buffers
//	SmackBufferClose(pSmack->SmackBuffer);

	// Close the smack flic
	BinkClose(pBink->BinkHandle);

	// Attempt opening the filename
	FileClose(pBink->hFileHandle);

	// Zero the memory, flags, etc.
	memset( pBink, 0, sizeof(BINKFLIC) );
}


BOOLEAN			BinkPollFlics(void)
{
	UINT32 uiCount;
	BOOLEAN fFlicStatus=FALSE;
	DDSURFACEDESC SurfaceDescription;
	BINKFLIC *pBink=NULL;
	UINT32	uiCopyToBufferFlags = guiBinkPixelFormat;

	//loop through all the open flics
	for(uiCount=0; uiCount < BINK_NUM_FLICS; uiCount++)
	{
		pBink = &BinkList[uiCount];

		if( pBink->uiFlags & BINK_FLIC_PLAYING )
		{
			fFlicStatus = TRUE;

			//do we still have to wait for the frame to be finished being displayed
			if( !( BinkWait( pBink->BinkHandle ) ) )
			{
				DDLockSurface( pBink->lpDDS, NULL, &SurfaceDescription, 0, NULL);

				BinkDoFrame( pBink->BinkHandle );

				BinkCopyToBuffer( pBink->BinkHandle, 
													SurfaceDescription.lpSurface,
													SurfaceDescription.lPitch,
													pBink->BinkHandle->Height,
													pBink->uiLeft,
													pBink->uiTop,
													uiCopyToBufferFlags );


				DDUnlockSurface( pBink->lpDDS, SurfaceDescription.lpSurface);

				// Check to see if the flic is done the last frame
				if( pBink->BinkHandle->FrameNum == ( pBink->BinkHandle->Frames-1 ) )
				{
					// If flic is looping, reset frame to 0
					if( pBink->uiFlags & BINK_FLIC_LOOP)
					{
						BinkGoto( pBink->BinkHandle, 0, 0 );
					}
					else if( pBink->uiFlags & BINK_FLIC_AUTOCLOSE)
					{
						BinkCloseFlic( pBink );
					}
				}
				else
				{
					BinkNextFrame( BinkList[uiCount].BinkHandle );
				}

			}
		}
	}

	return( fFlicStatus );
}



void				BinkSetupVideo(void)
{
	DDSURFACEDESC SurfaceDescription;
	HRESULT ReturnCode;
	UINT16 usRed, usGreen, usBlue;
	HVSURFACE hVSurface;

	GetVideoSurface( &hVSurface, FRAME_BUFFER );

	lpBinkVideoPlayback2 = GetVideoSurfaceDDSurface( hVSurface );

  ZEROMEM(SurfaceDescription);
  SurfaceDescription.dwSize = sizeof (DDSURFACEDESC);

  ReturnCode = IDirectDrawSurface2_GetSurfaceDesc ( lpBinkVideoPlayback2, &SurfaceDescription );
  if (ReturnCode != DD_OK)
  {
    DirectXAttempt ( ReturnCode, __LINE__, __FILE__ );
    return;
  }
 /* 
	usRed   = (UINT16) SurfaceDescription.ddpfPixelFormat.dwRBitMask;
	usGreen = (UINT16) SurfaceDescription.ddpfPixelFormat.dwGBitMask;
	usBlue  = (UINT16) SurfaceDescription.ddpfPixelFormat.dwBBitMask;

//	SurfaceDescription.ddpfPixelFormat

	if((usRed==0xf800) && (usGreen==0x07e0) && (usBlue==0x001f))
		guiBinkPixelFormat = BINKSURFACE565;
	else
		guiBinkPixelFormat = BINKSURFACE555;
*/
	//
	// Get bit count for the RGB
	//
	usRed = GetNumberOfBits( SurfaceDescription.ddpfPixelFormat.dwRBitMask );
	usGreen = GetNumberOfBits( SurfaceDescription.ddpfPixelFormat.dwGBitMask );
	usBlue = GetNumberOfBits( SurfaceDescription.ddpfPixelFormat.dwBBitMask );

	// 555
	if( usRed == 5 && usGreen == 5 && usBlue == 5 )
	{
		guiBinkPixelFormat = BINKSURFACE555;
	}
	//565
	else if( usRed == 5 && usGreen == 6 && usBlue == 5 )
	{
		guiBinkPixelFormat = BINKSURFACE565;
	}
	//655
	else if( usRed == 6 && usGreen == 5 && usBlue == 5 )
	{
		guiBinkPixelFormat = BINKSURFACE655;
	}

	//dont know the format, wont get video
	else
	{
		guiBinkPixelFormat = 0;
	}
}

UINT16 GetNumberOfBits( UINT32 uiMask )
{
  UINT16 usBits = 0;

  while( uiMask )
  {
      uiMask = uiMask & ( uiMask - 1 );  
      usBits++;
  }
  return usBits;
}
 

void				BinkShutdownVideo(void)
{
}



