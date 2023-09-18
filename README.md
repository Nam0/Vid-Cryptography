
# Python Video-Cryptography

This project was inspired by some reddit post I saw ages ago where a guy used QR codes to store data on youtube.

I don't intend for other to use this as it's probably against Google TOS, I didn't check however I'm assuming it is as they dont apperciate bot uploads which this would most likely be used for. I do intend to fix some issues with it currently. 

1. How to use incase you wanna do that for what ever reason.
    - Run the Encode.py file enter the full name of the file you'd wish to slice
    - Run the Vid.py file and convert that bad boy to a video you can store(it will be like 9 times the size due to awful compression and what not yk how it is.)
    - Dont upload to youtube
    - Dont download the video from youtube
    - Rename the file to what ever I put the test var to be set to in Slice.py
    - Finally run Decoder.py and get the original file back(mostly)
        - if needed there is a Bindump file to check the new against the OG file to see what happened.


1. Need to Fix
   - Easier use like one program 
        - selectable options for whats going on Encode/Decode no need for the middle ment
   - More Streamlined ofc
   - Speed issues as it is rather slow to process larger files, threading is kinda dookie tho with this use case especially when dealing with smaller files.
   - Better bit flip prevention idk what causes it other than pixels getting read incorrectly TBD there.


