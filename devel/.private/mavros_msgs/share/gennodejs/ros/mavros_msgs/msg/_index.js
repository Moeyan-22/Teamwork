
"use strict";

let WheelOdomStamped = require('./WheelOdomStamped.js');
let Trajectory = require('./Trajectory.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let CellularStatus = require('./CellularStatus.js');
let LogEntry = require('./LogEntry.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let MountControl = require('./MountControl.js');
let RadioStatus = require('./RadioStatus.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let ESCStatus = require('./ESCStatus.js');
let Tunnel = require('./Tunnel.js');
let HilGPS = require('./HilGPS.js');
let RCOut = require('./RCOut.js');
let StatusText = require('./StatusText.js');
let ManualControl = require('./ManualControl.js');
let Mavlink = require('./Mavlink.js');
let CommandCode = require('./CommandCode.js');
let WaypointReached = require('./WaypointReached.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let RTCM = require('./RTCM.js');
let BatteryStatus = require('./BatteryStatus.js');
let ESCInfo = require('./ESCInfo.js');
let PositionTarget = require('./PositionTarget.js');
let ActuatorControl = require('./ActuatorControl.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let HilControls = require('./HilControls.js');
let RTKBaseline = require('./RTKBaseline.js');
let Waypoint = require('./Waypoint.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let RCIn = require('./RCIn.js');
let State = require('./State.js');
let Param = require('./Param.js');
let Altitude = require('./Altitude.js');
let TerrainReport = require('./TerrainReport.js');
let LandingTarget = require('./LandingTarget.js');
let FileEntry = require('./FileEntry.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let WaypointList = require('./WaypointList.js');
let GPSINPUT = require('./GPSINPUT.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let ExtendedState = require('./ExtendedState.js');
let VFR_HUD = require('./VFR_HUD.js');
let DebugValue = require('./DebugValue.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let HomePosition = require('./HomePosition.js');
let GPSRAW = require('./GPSRAW.js');
let ParamValue = require('./ParamValue.js');
let LogData = require('./LogData.js');
let Thrust = require('./Thrust.js');
let VehicleInfo = require('./VehicleInfo.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let Vibration = require('./Vibration.js');
let HilSensor = require('./HilSensor.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let GPSRTK = require('./GPSRTK.js');

module.exports = {
  WheelOdomStamped: WheelOdomStamped,
  Trajectory: Trajectory,
  CameraImageCaptured: CameraImageCaptured,
  CamIMUStamp: CamIMUStamp,
  PlayTuneV2: PlayTuneV2,
  CellularStatus: CellularStatus,
  LogEntry: LogEntry,
  TimesyncStatus: TimesyncStatus,
  HilActuatorControls: HilActuatorControls,
  MountControl: MountControl,
  RadioStatus: RadioStatus,
  GlobalPositionTarget: GlobalPositionTarget,
  ESCStatus: ESCStatus,
  Tunnel: Tunnel,
  HilGPS: HilGPS,
  RCOut: RCOut,
  StatusText: StatusText,
  ManualControl: ManualControl,
  Mavlink: Mavlink,
  CommandCode: CommandCode,
  WaypointReached: WaypointReached,
  OverrideRCIn: OverrideRCIn,
  RTCM: RTCM,
  BatteryStatus: BatteryStatus,
  ESCInfo: ESCInfo,
  PositionTarget: PositionTarget,
  ActuatorControl: ActuatorControl,
  ESCTelemetryItem: ESCTelemetryItem,
  AttitudeTarget: AttitudeTarget,
  HilControls: HilControls,
  RTKBaseline: RTKBaseline,
  Waypoint: Waypoint,
  NavControllerOutput: NavControllerOutput,
  RCIn: RCIn,
  State: State,
  Param: Param,
  Altitude: Altitude,
  TerrainReport: TerrainReport,
  LandingTarget: LandingTarget,
  FileEntry: FileEntry,
  CompanionProcessStatus: CompanionProcessStatus,
  WaypointList: WaypointList,
  GPSINPUT: GPSINPUT,
  HilStateQuaternion: HilStateQuaternion,
  MagnetometerReporter: MagnetometerReporter,
  ExtendedState: ExtendedState,
  VFR_HUD: VFR_HUD,
  DebugValue: DebugValue,
  ADSBVehicle: ADSBVehicle,
  HomePosition: HomePosition,
  GPSRAW: GPSRAW,
  ParamValue: ParamValue,
  LogData: LogData,
  Thrust: Thrust,
  VehicleInfo: VehicleInfo,
  ESCStatusItem: ESCStatusItem,
  OnboardComputerStatus: OnboardComputerStatus,
  ESCInfoItem: ESCInfoItem,
  EstimatorStatus: EstimatorStatus,
  Vibration: Vibration,
  HilSensor: HilSensor,
  ESCTelemetry: ESCTelemetry,
  OpticalFlowRad: OpticalFlowRad,
  GPSRTK: GPSRTK,
};
