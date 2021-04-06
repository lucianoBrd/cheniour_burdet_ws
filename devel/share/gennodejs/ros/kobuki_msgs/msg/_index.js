
"use strict";

let WheelDropEvent = require('./WheelDropEvent.js');
let ControllerInfo = require('./ControllerInfo.js');
let BumperEvent = require('./BumperEvent.js');
let Sound = require('./Sound.js');
let ExternalPower = require('./ExternalPower.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let ButtonEvent = require('./ButtonEvent.js');
let VersionInfo = require('./VersionInfo.js');
let Led = require('./Led.js');
let SensorState = require('./SensorState.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let CliffEvent = require('./CliffEvent.js');
let KeyboardInput = require('./KeyboardInput.js');
let MotorPower = require('./MotorPower.js');
let DigitalOutput = require('./DigitalOutput.js');
let ScanAngle = require('./ScanAngle.js');
let PowerSystemEvent = require('./PowerSystemEvent.js');
let DockInfraRed = require('./DockInfraRed.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingResult = require('./AutoDockingResult.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');
let AutoDockingAction = require('./AutoDockingAction.js');

module.exports = {
  WheelDropEvent: WheelDropEvent,
  ControllerInfo: ControllerInfo,
  BumperEvent: BumperEvent,
  Sound: Sound,
  ExternalPower: ExternalPower,
  RobotStateEvent: RobotStateEvent,
  ButtonEvent: ButtonEvent,
  VersionInfo: VersionInfo,
  Led: Led,
  SensorState: SensorState,
  DigitalInputEvent: DigitalInputEvent,
  CliffEvent: CliffEvent,
  KeyboardInput: KeyboardInput,
  MotorPower: MotorPower,
  DigitalOutput: DigitalOutput,
  ScanAngle: ScanAngle,
  PowerSystemEvent: PowerSystemEvent,
  DockInfraRed: DockInfraRed,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingActionGoal: AutoDockingActionGoal,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingResult: AutoDockingResult,
  AutoDockingFeedback: AutoDockingFeedback,
  AutoDockingAction: AutoDockingAction,
};
