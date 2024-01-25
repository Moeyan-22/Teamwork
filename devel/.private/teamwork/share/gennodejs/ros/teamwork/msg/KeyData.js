// Auto-generated. Do not edit!

// (in-package teamwork.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class KeyData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.router_key = null;
      this.display_key = null;
    }
    else {
      if (initObj.hasOwnProperty('router_key')) {
        this.router_key = initObj.router_key
      }
      else {
        this.router_key = '';
      }
      if (initObj.hasOwnProperty('display_key')) {
        this.display_key = initObj.display_key
      }
      else {
        this.display_key = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type KeyData
    // Serialize message field [router_key]
    bufferOffset = _serializer.string(obj.router_key, buffer, bufferOffset);
    // Serialize message field [display_key]
    bufferOffset = _serializer.string(obj.display_key, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type KeyData
    let len;
    let data = new KeyData(null);
    // Deserialize message field [router_key]
    data.router_key = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [display_key]
    data.display_key = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.router_key);
    length += _getByteLength(object.display_key);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'teamwork/KeyData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '479cab83ef8c9b1034cf5fc201002f01';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # KeyData.msg
    string router_key
    string display_key
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new KeyData(null);
    if (msg.router_key !== undefined) {
      resolved.router_key = msg.router_key;
    }
    else {
      resolved.router_key = ''
    }

    if (msg.display_key !== undefined) {
      resolved.display_key = msg.display_key;
    }
    else {
      resolved.display_key = ''
    }

    return resolved;
    }
};

module.exports = KeyData;
