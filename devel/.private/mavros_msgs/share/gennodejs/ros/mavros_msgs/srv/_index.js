
"use strict";

let MountConfigure = require('./MountConfigure.js')
let FileWrite = require('./FileWrite.js')
let ParamSet = require('./ParamSet.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let FileList = require('./FileList.js')
let CommandBool = require('./CommandBool.js')
let LogRequestData = require('./LogRequestData.js')
let ParamPush = require('./ParamPush.js')
let CommandTOL = require('./CommandTOL.js')
let FileRead = require('./FileRead.js')
let WaypointClear = require('./WaypointClear.js')
let SetMode = require('./SetMode.js')
let CommandHome = require('./CommandHome.js')
let CommandAck = require('./CommandAck.js')
let FileChecksum = require('./FileChecksum.js')
let ParamPull = require('./ParamPull.js')
let FileOpen = require('./FileOpen.js')
let WaypointPull = require('./WaypointPull.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let FileClose = require('./FileClose.js')
let FileRename = require('./FileRename.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let FileTruncate = require('./FileTruncate.js')
let MessageInterval = require('./MessageInterval.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let SetMavFrame = require('./SetMavFrame.js')
let FileMakeDir = require('./FileMakeDir.js')
let FileRemove = require('./FileRemove.js')
let StreamRate = require('./StreamRate.js')
let WaypointPush = require('./WaypointPush.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let CommandInt = require('./CommandInt.js')
let CommandLong = require('./CommandLong.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let LogRequestList = require('./LogRequestList.js')
let ParamGet = require('./ParamGet.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')

module.exports = {
  MountConfigure: MountConfigure,
  FileWrite: FileWrite,
  ParamSet: ParamSet,
  FileRemoveDir: FileRemoveDir,
  FileList: FileList,
  CommandBool: CommandBool,
  LogRequestData: LogRequestData,
  ParamPush: ParamPush,
  CommandTOL: CommandTOL,
  FileRead: FileRead,
  WaypointClear: WaypointClear,
  SetMode: SetMode,
  CommandHome: CommandHome,
  CommandAck: CommandAck,
  FileChecksum: FileChecksum,
  ParamPull: ParamPull,
  FileOpen: FileOpen,
  WaypointPull: WaypointPull,
  LogRequestEnd: LogRequestEnd,
  FileClose: FileClose,
  FileRename: FileRename,
  CommandTriggerControl: CommandTriggerControl,
  FileTruncate: FileTruncate,
  MessageInterval: MessageInterval,
  CommandVtolTransition: CommandVtolTransition,
  SetMavFrame: SetMavFrame,
  FileMakeDir: FileMakeDir,
  FileRemove: FileRemove,
  StreamRate: StreamRate,
  WaypointPush: WaypointPush,
  CommandTriggerInterval: CommandTriggerInterval,
  CommandInt: CommandInt,
  CommandLong: CommandLong,
  VehicleInfoGet: VehicleInfoGet,
  LogRequestList: LogRequestList,
  ParamGet: ParamGet,
  WaypointSetCurrent: WaypointSetCurrent,
};
