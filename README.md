# Simple Testscenario for [Issue #186](https://github.com/miguelgrinberg/Flask-SocketIO/issues/186) of flask-socketIO

The problem is already described in the issue, but a brief summary how it is for me:

When firefox tries to upgrade from polling to websockets sometimes only the first round of "probe" messages is send (2probe from client and 3probe from server, when looking at the websocket communication in firefox), but not the third message ("5"). After refreshing (sometimes up to 10 times), a connection is established correctly.

In this small example, nothing happens when clicking the Test-Button, which would emit a message to the server which then returns it, which would then be displayed in a div, when the connection is not established correctly.


