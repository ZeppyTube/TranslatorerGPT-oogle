# TranslatorerGPT-oogle
 A real(ish) time translator app powered by Google translate
 !!DISCLAIMER!! MOST OF THIS CODE (97% OF IT) WAS MADE USING CHATGPT, I (ZEPPYTUBE) ONLY FIXED SOME OF IT. I AM NOT A CODER.

 This app translates text you write in any text field to your selected output text, the options are:
 
 `Arabic, Bengali, Chinese Simplified, Chinese Traditional, Dutch, English, Estonian, French, German, Gujarati, Hebrew, Hindi, Indonesian, Italian, Japanese, Japanese Romanji, Kannada, Korean, Malay, Marathi, Norwegian, Polish, Portuguese, Punjabi, Russian, Spanish, Tamil, Telugu, Thai, Turkish, Urdu, Vietnamese and Welsh.`
 
 You can add more languages if you want by editing the settings.py file
 
 The only language that's a bit broken is japanese romanji, as you can see there's a romanji.json file, this is because I couldn't get romkan to work and just did it manually (as in forced chatgpt to do it lol)

#
 
 To run this app you can either download the source code and just install python and the independences, the script for that is (In a CMD window):
 
 `pip install googletrans==4.0.0-rc1 tk pystray Pillow keyboard requests` then run the `main.py` file
 
 Or you can just download the exe file and run that, you don't even need python installed run it (Windows defender might flag it, so if your scared of that just run the source code)

# ACTUAL USE

When using the app, you just open it, input your output language, then start typing anywhere and when it detects you stop typing for a full second, it'll replace the text with the translated text

# 

 Some more notes:
 - This requires a internet connection because it needs to connect to google's api
 - This might flag anticheat if your using this to text in game chats, because this is technically a macro script, so please turn off the app if you don't want to be banned (Idk why you would use this anyways it's legit a proof of concept xd)
