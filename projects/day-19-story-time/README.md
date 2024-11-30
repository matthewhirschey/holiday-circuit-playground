# Day 19: Holiday Story Time

## Overview
Today we'll create a holiday story player using our STEMMA Speaker! We'll use both pre-recorded holiday stories and generated sounds to create an interactive audio experience. The younger group will control story playback, while the older group will program complex audio sequences with effects.

## Materials Needed
- Circuit Playground Express
- STEMMA Speaker
- Mini Breadboard
- Alligator Clips
- Story box materials
- USB Cable
- Computer for file transfer

## Required Audio Files
- `holiday_story.wav` (provided) - A short holiday story in WAV format
- Note: The story file should be 16-bit, 22050 Hz, mono WAV format for best compatibility

## Instructions for Age 9

1. Connect Your Speaker:
   - Red wire to 3.3V
   - Black wire to GND
   - White wire to A1

2. Load the Story File:
   - Connect Circuit Playground Express to computer
   - It will appear as a USB drive called CIRCUITPY
   - Copy `holiday_story.wav` to the CIRCUITPY drive
   - Wait for file transfer to complete
   - The built-in LED will stop flashing when ready

3. Create Story Box:
   - Decorate a box for your player
   - Add button labels:
     - A: Play Story
     - B: Play Sound Effects
     - A+B: Special Surprise!
   - Make holes for the speaker
   - Add holiday decorations

4. Test Your Player:
   - Press A to play the story
   - Press B for sound effects
   - Press both buttons for a surprise
   - Use switch for volume control

5. Tell Your Story:
   - Practice the timing with the audio
   - Add gestures and movements
   - Create a special story area

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection instructions
   - Consider speaker placement for best sound
   - Think about LED placement for effects

2. File Preparation:
   - Story file must be WAV format (16-bit, 22050 Hz, mono)
   - If you have an MP3, convert it using Audacity:
     1. Open MP3 in Audacity
     2. Click File → Export → Export as WAV
     3. Select 'WAV (Microsoft)'
     4. Choose '16-bit PCM'
     5. Set Project Rate to 22050 Hz
     6. Save as 'holiday_story.wav'

3. Advanced Features:
   - Create multiple sound sequences
   - Add light effects
   - Use sensors for interactive playback
   - Program environmental effects

## Testing and Troubleshooting

### For 9-Year-Olds:
1. No Sound?
   - Check speaker connections
   - Verify file is on CIRCUITPY drive
   - Try adjusting volume switch
   - Reset the board

2. File Won't Copy?
   - Check file name (holiday_story.wav)
   - Ensure file format is correct
   - Try ejecting and reconnecting drive
   - Make sure drive has space

### For 13-Year-Olds:
1. Audio Issues?
   - Verify WAV format settings
   - Check playback timing
   - Debug effects mixing
   - Monitor memory usage

2. Code Problems?
   - Print debug messages
   - Test file operations
   - Verify event triggers
   - Check sensor readings

## Extensions

### For 9-Year-Olds:
1. Create story cards
2. Add character voices
3. Make sound effect buttons
4. Design a story scene

### For 13-Year-Olds:
1. Add motion triggers
2. Create branching stories
3. Synchronize LED patterns
4. Add environmental effects
5. Create interactive elements

## Safety Notes
- Keep volume at reasonable levels
- Handle connections carefully
- Mind the speaker placement
- Keep electronics dry

## Parent Notes

### Setup Help
- Assist with file transfer
- Guide proper volume levels
- Help with connections
- Support creative ideas

### Circuit Playground Tips
- Files must be in correct format
- Drive may need to be ejected properly
- Board may need reset after file transfer
- Save code before copying files

### Story Creation
- Help choose appropriate content
- Guide timing and pacing
- Support sound effects ideas
- Encourage creativity