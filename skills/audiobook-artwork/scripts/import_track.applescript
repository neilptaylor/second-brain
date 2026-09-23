-- Imports a single MP3 into Music.app, sets metadata, and embeds artwork.
-- Called once per chapter by build_audiobook.py. Not meant to be run by hand.
--
-- argv: mp3Path, imgPath, trackTitle, artistName, albumName, genreName, yearVal, trackNum, trackCount

on run argv
	set mp3Path to item 1 of argv
	set imgPath to item 2 of argv
	set trackTitle to item 3 of argv
	set artistName to item 4 of argv
	set albumName to item 5 of argv
	set genreName to item 6 of argv
	set yearVal to (item 7 of argv) as integer
	set trackNum to (item 8 of argv) as integer
	set trackCount to (item 9 of argv) as integer

	set mp3File to POSIX file mp3Path
	set imgFile to POSIX file imgPath

	tell application "Music"
		set newTrack to add mp3File
		set artData to read imgFile as picture

		-- Large files stay "busy" in Music for a few seconds after import
		-- (it's still copying/analysing them), so setting properties right
		-- away can fail with "File some object is busy" (-47). Retry.
		set tries to 0
		repeat
			try
				set name of newTrack to trackTitle
				set artist of newTrack to artistName
				set album of newTrack to albumName
				set genre of newTrack to genreName
				set year of newTrack to yearVal
				set track number of newTrack to trackNum
				set track count of newTrack to trackCount
				set data of artwork 1 of newTrack to artData
				exit repeat
			on error errMsg
				set tries to tries + 1
				if tries > 60 then error "gave up waiting for Music to finish importing: " & errMsg
				delay 2
			end try
		end repeat
	end tell

	return "OK"
end run
