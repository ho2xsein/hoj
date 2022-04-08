from pyrogram import filters, Client


ids = 17219899 #put api id
hash = "926652414fe0f495a1a57426319140a5" #put api hash

app = Client("SessionName", api_id=ids, api_hash=hash)




@app.on_message(filters.channel)
def sendchnl(c,m):
    channel = "@zaskoi" 
    with open("list.txt", "r" , encoding="utf8") as file:
        lines = [line.rstrip() for line in file]
    for ilin in lines:
        try:
            if ilin in m.text:
                app.forward_messages(channel, m.sender_chat.id, m.message_id)
                break
        except:
            if ilin in m.caption:
                app.forward_messages(channel, m.sender_chat.id, m.message_id)
                break




app.run()
