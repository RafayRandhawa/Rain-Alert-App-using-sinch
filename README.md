You can get your own open weather API key bygoinf onto https://openweathermap.org/ and signing up for a free account, from there you will need to proceed to their API section.
You can get your own latitude and longitude coordinates from https://www.latlong.net/.
For easily viewing and understanding the format of the json data recieved you can paste your json data here: https://jsonviewer.stack.hu/.
For being able to use sinch you will need to go to sinch and sign up for a account. The account can be free or paid depending on your needs.
On the sinch website make a project and then under that project go to settings->access keys to get project id, app id and get a secret key (this will only be provided once so make sure to save it somewhere).
Now replace the data field in the code with what you've recieved from sinch, you can get your sinch number from sms->getting started.
Note that this code makes use of the sinch SDK, but you can also use the sinch REST API.
SDK help documentation: https://developers.sinch.com/docs/sms/getting-started/python/send-sms-sdk/.
REST API help: https://www.youtube.com/watch?v=kw2K9RCWxaA, https://developers.sinch.com/docs/sms/getting-started/python/python-send-sms/.
