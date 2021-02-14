# Chatbot

Train chatbot on your Telegram chat.

## Steps:

1.  Export chat history in the *Group info* menu:

    ![](images/1.png)

2.  Open your Google Drive, create *chatbot_data* folder, and put result.json there:

    ![](images/2.png)

3.  Open [train_chatbot.ipynb](https://colab.research.google.com/github/vinnik-dmitry07/Chatbot/blob/main/train_chatbot.ipynb)

4. Go to *Runtime > Run all*

5.  Mount your drive (press enter after pasting a code):

    ![](images/3.png) 
    
6. After training have started do not close the browser tab until you go out of the quota (about 10 hours)

7. Open [run_chatbot.ipynb](https://colab.research.google.com/github/vinnik-dmitry07/Chatbot/blob/main/run_chatbot.ipynb)

8. Run setup cells (installing parlai, mounting the drive)

9.  Run this cell to show what model answers on the test data:
    
    ![](images/4.png)
    
    ![](images/5.png)
    
    ("labels" is what the model was training to answer, "model" is actual model output)
    
10.  To chat with the model run this cell:
    
    ![](images/6.png)