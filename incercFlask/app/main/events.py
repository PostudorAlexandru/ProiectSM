from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = 'Chatroom'
    join_room(room)
    emit('status', {'msg': 'Alex ' + ' has entered the room.'}, room=room)


@socketio.on('text')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = 'Chatroom'
    print(message['msg'])
    emit('message', {'msg': 'Alex' + ':' + message['msg']}, room=room)


@socketio.on('left')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': 'Alex' + ' has left the room.'}, room=room)

