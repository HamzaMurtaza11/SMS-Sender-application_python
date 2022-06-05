from twilio.rest import Client 
 
account_sid = 'TWILIO ACCOUNT SID HERE' 
auth_token = 'TWILIO AUTH TOKEN HERE' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='TWILIO MESSAGING SERVICE ID HERE', 
                              body='Hi, HAMZA MURTAZA here.',      
                              to='enter phone number here whom you gonna send message.' 
                          ) 
 
print(message.sid)