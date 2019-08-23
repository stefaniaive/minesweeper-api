# minesweeper

// I will be documenting the API services here because of time but is nice to have swagger integration.


*POST* /api/minesweeper

Headers 

    Content-Type: application/json
    
Payload

    {
        "sizeX": Integer // The row size
        "sizeY": Integer // The col size
        "Mines": Integer // Cant Mines - Must be lower than dimension
    }

 
Responses:

    201 CREATED
        {
            "id": UUID  // Minesweeper id
        }
        
    
    400 BAD REQUEST
    
        - When the mines are lower than dimention 
        - When X/Y are 0
        
        

*PATCH* /api/minesweeper/ID

Headers 

    Content-Type: application/json
    
Payload

    {
        "posX": Integer // The cell row 
        "posY": Integer // The cell col
    }

 
Responses:

    200 OK
        {
           "lost": false, 
           "wined": false, 
           "turnedCells": [
                 { "posX": Integer,
                   "posY": Integer,
                   "value": Integer}
           ]}
        }
    
    - Lost or wined will be True when the game ends. 
    - Turned cells have the list of cells with their values which was turned with the current movement
    
    
    
SERVICE NICE TO HAVE:

*GET* /api/minesweeper/id

This will return the current status of bord with visible cells. 
Usefull if the app turn off and lost the state.

