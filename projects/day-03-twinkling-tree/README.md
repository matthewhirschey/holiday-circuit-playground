# Day 3: Twinkling Holiday Tree

## Overview
Transform your wooden Christmas tree into a glowing masterpiece! Today we'll add LEDs and a tactile switch to make your tree light up with festive joy. You'll learn about switches and how to create lighting patterns.

## Materials Needed
- Balsa wood tree cutout (or thick cardstock)
- Multiple LEDs (various colors)
- Tactile button switch
- Circuit Playground Express
- Copper tape
- Decorating supplies

## Instructions for Age 9

1. Prepare Your Tree:
   - Take your balsa wood tree cutout
   - Decorate it with markers or stickers
   - Plan where your LEDs will go

2. Set Up LEDs:
   - Place LEDs into the holes (or tape along edges)
   - Make sure longer legs (positive) are all on one side
   - Shorter legs (negative) should be on the other side

3. Create the Circuit:
   - Use copper tape on the back to connect positive LED legs
   - Connect negative LED legs with another strip
   - Add the tactile button switch in the middle

```svg
   <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
     <!-- Background -->
     <rect width="400" height="300" fill="#f8f9fa"/>
     
     <!-- Title -->
     <text x="200" y="30" text-anchor="middle" font-size="16" font-weight="bold">Tactile Button Switch Connection</text>
     
     <!-- Button Switch -->
     <rect x="160" y="120" width="80" height="80" fill="#d4d4d4" stroke="#333" stroke-width="2"/>
     <circle cx="200" cy="160" r="25" fill="#888"/>
     <circle cx="200" cy="160" r="20" fill="#666"/>
     
     <!-- Copper Tape Lines -->
     <path d="M 100,160 L 160,160" stroke="#cd7f32" stroke-width="8" fill="none"/>
     <path d="M 240,160 L 300,160" stroke="#cd7f32" stroke-width="8" fill="none"/>
     
     <!-- Labels -->
     <text x="130" y="150" text-anchor="middle" font-size="12">Copper Tape</text>
     <text x="270" y="150" text-anchor="middle" font-size="12">Copper Tape</text>
     <text x="200" y="230" text-anchor="middle" font-size="12">Tactile Button</text>
     
     <!-- Pin Labels -->
     <text x="170" y="110" text-anchor="middle" font-size="10">Pin 1</text>
     <text x="230" y="110" text-anchor="middle" font-size="10">Pin 2</text>
     <text x="170" y="220" text-anchor="middle" font-size="10">Pin 3</text>
     <text x="230" y="220" text-anchor="middle" font-size="10">Pin 4</text>
   </svg>
```

4. Connect Power:
   - Attach battery positive to one side
   - Connect negative to the other side
   - Test by pressing the button!

## Instructions for Age 13

1. Advanced Circuit Design:
   - Design parallel LED connections
   - Create multiple light patterns
   - Add brightness control

## Circuit Testing
1. Test each LED individually
2. Verify switch operation
3. Check all connections
4. Test different patterns

## Troubleshooting
- LEDs not lighting?
  - Check LED polarity
  - Verify copper tape connections
  - Test button functionality
  - Check power connections

## Extensions
1. Add more LED patterns
2. Create multiple switches
3. Add sound effects
4. Incorporate motion sensors

## Safety Notes
- Handle wood/cardstock carefully
- Mind sharp edges
- Proper tool usage
- Adult supervision needed

## Parent Notes
- Assist with wood/cardstock cutting
- Help test circuits
- Guide switch placement
- Monitor tool usage
