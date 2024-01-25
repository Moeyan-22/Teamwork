; Auto-generated. Do not edit!


(cl:in-package teamwork-msg)


;//! \htmlinclude KeyData.msg.html

(cl:defclass <KeyData> (roslisp-msg-protocol:ros-message)
  ((router_key
    :reader router_key
    :initarg :router_key
    :type cl:string
    :initform "")
   (display_key
    :reader display_key
    :initarg :display_key
    :type cl:string
    :initform ""))
)

(cl:defclass KeyData (<KeyData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <KeyData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'KeyData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name teamwork-msg:<KeyData> is deprecated: use teamwork-msg:KeyData instead.")))

(cl:ensure-generic-function 'router_key-val :lambda-list '(m))
(cl:defmethod router_key-val ((m <KeyData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader teamwork-msg:router_key-val is deprecated.  Use teamwork-msg:router_key instead.")
  (router_key m))

(cl:ensure-generic-function 'display_key-val :lambda-list '(m))
(cl:defmethod display_key-val ((m <KeyData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader teamwork-msg:display_key-val is deprecated.  Use teamwork-msg:display_key instead.")
  (display_key m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <KeyData>) ostream)
  "Serializes a message object of type '<KeyData>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'router_key))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'router_key))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'display_key))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'display_key))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <KeyData>) istream)
  "Deserializes a message object of type '<KeyData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'router_key) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'router_key) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'display_key) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'display_key) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<KeyData>)))
  "Returns string type for a message object of type '<KeyData>"
  "teamwork/KeyData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'KeyData)))
  "Returns string type for a message object of type 'KeyData"
  "teamwork/KeyData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<KeyData>)))
  "Returns md5sum for a message object of type '<KeyData>"
  "479cab83ef8c9b1034cf5fc201002f01")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'KeyData)))
  "Returns md5sum for a message object of type 'KeyData"
  "479cab83ef8c9b1034cf5fc201002f01")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<KeyData>)))
  "Returns full string definition for message of type '<KeyData>"
  (cl:format cl:nil "# KeyData.msg~%string router_key~%string display_key~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'KeyData)))
  "Returns full string definition for message of type 'KeyData"
  (cl:format cl:nil "# KeyData.msg~%string router_key~%string display_key~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <KeyData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'router_key))
     4 (cl:length (cl:slot-value msg 'display_key))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <KeyData>))
  "Converts a ROS message object to a list"
  (cl:list 'KeyData
    (cl:cons ':router_key (router_key msg))
    (cl:cons ':display_key (display_key msg))
))
