#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Tue Jan 14 16:42:38 2020
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'CvE_Comparison_PP3'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexviegut/Box/0...AAV...0/PROJECT_OTHER/Comparison_vs_Estimation/Design/PsychoPy_ComparisonExperiment/CvE_Comparison_PP3.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[192, 192, 192], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrImages1 = visual.ImageStim(
    win=win,
    name='instrImages1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, .5625),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixCross = visual.TextStim(win=win, name='fixCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimLeft = visual.ImageStim(
    win=win,
    name='stimLeft', 
    image='sin', mask=None,
    ori=0, pos=(.2, 0), size=(.3175, .5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stimRight = visual.ImageStim(
    win=win,
    name='stimRight', 
    image='sin', mask=None,
    ori=0, pos=(-.2, 0), size=(.3175, .5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
goodJob = visual.TextStim(win=win, name='goodJob',
    text='Great job! You are ready for the next activity.\n\nPlease let the experimenter know.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CvE_CompInstructions.xlsx'),
    seed=None, name='instructions')
thisExp.addLoop(instructions)  # add the loop to the experiment
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    t = 0
    instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instrImages1.setImage(instrImage)
    key_resp_instr = keyboard.Keyboard()
    # keep track of which components have finished
    instrComponents = [instrImages1, key_resp_instr]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrImages1* updates
        if t >= 0.0 and instrImages1.status == NOT_STARTED:
            # keep track of start time/frame for later
            instrImages1.tStart = t  # not accounting for scr refresh
            instrImages1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instrImages1, 'tStartRefresh')  # time at next scr refresh
            instrImages1.setAutoDraw(True)
        
        # *key_resp_instr* updates
        if t >= 0.0 and key_resp_instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_instr.tStart = t  # not accounting for scr refresh
            key_resp_instr.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_instr, 'tStartRefresh')  # time at next scr refresh
            key_resp_instr.status = STARTED
            # keyboard checking is just starting
            key_resp_instr.clearEvents(eventType='keyboard')
        if key_resp_instr.status == STARTED:
            theseKeys = key_resp_instr.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions.addData('instrImages1.started', instrImages1.tStartRefresh)
    instructions.addData('instrImages1.stopped', instrImages1.tStopRefresh)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
trialLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CvE_CompBreaks.xlsx'),
    seed=None, name='trialLoop')
thisExp.addLoop(trialLoop)  # add the loop to the experiment
thisTrialLoop = trialLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
if thisTrialLoop != None:
    for paramName in thisTrialLoop:
        exec('{} = thisTrialLoop[paramName]'.format(paramName))

for thisTrialLoop in trialLoop:
    currentLoop = trialLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            exec('{} = thisTrialLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SectionFile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixCross]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixCross* updates
            if t >= 0.0 and fixCross.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixCross.tStart = t  # not accounting for scr refresh
                fixCross.frameNStart = frameN  # exact frame index
                win.timeOnFlip(fixCross, 'tStartRefresh')  # time at next scr refresh
                fixCross.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixCross.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                fixCross.tStop = t  # not accounting for scr refresh
                fixCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixCross, 'tStopRefresh')  # time at next scr refresh
                fixCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('fixCross.started', fixCross.tStartRefresh)
        trials.addData('fixCross.stopped', fixCross.tStopRefresh)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        stimLeft.setImage(stimLeftFile)
        stimRight.setImage(stimRightFile)
        decisionStim = keyboard.Keyboard()
        # keep track of which components have finished
        trialComponents = [stimLeft, stimRight, decisionStim]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimLeft* updates
            if t >= 0.0 and stimLeft.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimLeft.tStart = t  # not accounting for scr refresh
                stimLeft.frameNStart = frameN  # exact frame index
                win.timeOnFlip(stimLeft, 'tStartRefresh')  # time at next scr refresh
                stimLeft.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stimLeft.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                stimLeft.tStop = t  # not accounting for scr refresh
                stimLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimLeft, 'tStopRefresh')  # time at next scr refresh
                stimLeft.setAutoDraw(False)
            
            # *stimRight* updates
            if t >= 0.0 and stimRight.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimRight.tStart = t  # not accounting for scr refresh
                stimRight.frameNStart = frameN  # exact frame index
                win.timeOnFlip(stimRight, 'tStartRefresh')  # time at next scr refresh
                stimRight.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stimRight.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                stimRight.tStop = t  # not accounting for scr refresh
                stimRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimRight, 'tStopRefresh')  # time at next scr refresh
                stimRight.setAutoDraw(False)
            
            # *decisionStim* updates
            if t >= 0.0 and decisionStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                decisionStim.tStart = t  # not accounting for scr refresh
                decisionStim.frameNStart = frameN  # exact frame index
                win.timeOnFlip(decisionStim, 'tStartRefresh')  # time at next scr refresh
                decisionStim.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(decisionStim.clock.reset)  # t=0 on next screen flip
                decisionStim.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if decisionStim.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                decisionStim.tStop = t  # not accounting for scr refresh
                decisionStim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(decisionStim, 'tStopRefresh')  # time at next scr refresh
                decisionStim.status = FINISHED
            if decisionStim.status == STARTED:
                theseKeys = decisionStim.getKeys(keyList=['f', 'j'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    decisionStim.keys = theseKeys.name  # just the last key pressed
                    decisionStim.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('stimLeft.started', stimLeft.tStartRefresh)
        trials.addData('stimLeft.stopped', stimLeft.tStopRefresh)
        trials.addData('stimRight.started', stimRight.tStartRefresh)
        trials.addData('stimRight.stopped', stimRight.tStopRefresh)
        # check responses
        if decisionStim.keys in ['', [], None]:  # No response was made
            decisionStim.keys = None
        trials.addData('decisionStim.keys',decisionStim.keys)
        if decisionStim.keys != None:  # we had a response
            trials.addData('decisionStim.rt', decisionStim.rt)
        trials.addData('decisionStim.started', decisionStim.tStartRefresh)
        trials.addData('decisionStim.stopped', decisionStim.tStopRefresh)
        
        # ------Prepare to start Routine "blank"-------
        t = 0
        blankClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if decisionStim.keys != None:
            continueRoutine=False
        decisionBlank = keyboard.Keyboard()
        # keep track of which components have finished
        blankComponents = [textBlank, decisionBlank]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "blank"-------
        while continueRoutine:
            # get current time
            t = blankClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlank* updates
            if t >= 0.0 and textBlank.status == NOT_STARTED:
                # keep track of start time/frame for later
                textBlank.tStart = t  # not accounting for scr refresh
                textBlank.frameNStart = frameN  # exact frame index
                win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(True)
            
            # *decisionBlank* updates
            if t >= 0.0 and decisionBlank.status == NOT_STARTED:
                # keep track of start time/frame for later
                decisionBlank.tStart = t  # not accounting for scr refresh
                decisionBlank.frameNStart = frameN  # exact frame index
                win.timeOnFlip(decisionBlank, 'tStartRefresh')  # time at next scr refresh
                decisionBlank.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(decisionBlank.clock.reset)  # t=0 on next screen flip
                decisionBlank.clearEvents(eventType='keyboard')
            if decisionBlank.status == STARTED:
                theseKeys = decisionBlank.getKeys(keyList=['f', 'j'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    decisionBlank.keys = theseKeys.name  # just the last key pressed
                    decisionBlank.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blank"-------
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('textBlank.started', textBlank.tStartRefresh)
        trials.addData('textBlank.stopped', textBlank.tStopRefresh)
        # check responses
        if decisionBlank.keys in ['', [], None]:  # No response was made
            decisionBlank.keys = None
        trials.addData('decisionBlank.keys',decisionBlank.keys)
        if decisionBlank.keys != None:  # we had a response
            trials.addData('decisionBlank.rt', decisionBlank.rt)
        trials.addData('decisionBlank.started', decisionBlank.tStartRefresh)
        trials.addData('decisionBlank.stopped', decisionBlank.tStopRefresh)
        # the Routine "blank" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "Break"-------
    t = 0
    BreakClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    BreakText.setText(BreakSectionText)
    key_resp_break = keyboard.Keyboard()
    # keep track of which components have finished
    BreakComponents = [BreakText, key_resp_break]
    for thisComponent in BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Break"-------
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BreakText* updates
        if t >= 0.0 and BreakText.status == NOT_STARTED:
            # keep track of start time/frame for later
            BreakText.tStart = t  # not accounting for scr refresh
            BreakText.frameNStart = frameN  # exact frame index
            win.timeOnFlip(BreakText, 'tStartRefresh')  # time at next scr refresh
            BreakText.setAutoDraw(True)
        
        # *key_resp_break* updates
        if t >= 0.0 and key_resp_break.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_break.tStart = t  # not accounting for scr refresh
            key_resp_break.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_break, 'tStartRefresh')  # time at next scr refresh
            key_resp_break.status = STARTED
            # keyboard checking is just starting
            key_resp_break.clearEvents(eventType='keyboard')
        if key_resp_break.status == STARTED:
            theseKeys = key_resp_break.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialLoop.addData('BreakText.started', BreakText.tStartRefresh)
    trialLoop.addData('BreakText.stopped', BreakText.tStopRefresh)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trialLoop'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [goodJob]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodJob* updates
    if t >= 0.0 and goodJob.status == NOT_STARTED:
        # keep track of start time/frame for later
        goodJob.tStart = t  # not accounting for scr refresh
        goodJob.frameNStart = frameN  # exact frame index
        win.timeOnFlip(goodJob, 'tStartRefresh')  # time at next scr refresh
        goodJob.setAutoDraw(True)
    frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if goodJob.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        goodJob.tStop = t  # not accounting for scr refresh
        goodJob.frameNStop = frameN  # exact frame index
        win.timeOnFlip(goodJob, 'tStopRefresh')  # time at next scr refresh
        goodJob.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goodJob.started', goodJob.tStartRefresh)
thisExp.addData('goodJob.stopped', goodJob.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
