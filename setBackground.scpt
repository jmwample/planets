tell application "System Events"
    set desktopCount to count of desktops
    repeat with desktopNumber from 1 to desktopCount
        tell desktop desktopNumber
            set picture to "/users/jmwample/Dev/planets/drawing.png"
        end tell
    end repeat
end tell
