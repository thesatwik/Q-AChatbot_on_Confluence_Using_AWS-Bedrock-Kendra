# Create AWS Kendra Index and Add Confluence as Data Source. 

Following steps provide overview on how to create Kendra Index and then add Confluence as DataStore. 


## 1 Prepare Confluence token  

This step is required to create a confluence token which will be used by Kendra (in later steps) to connect and maintain periodic sync. 
Go to [https://id.atlassian.com/manage-profile/security/api-tokens], login with **admin credentials** and create an API Token. 

Details steps can be found [here](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token)

 **_NOTE:_**  For testing purpose, one can create a free confluence account and populate few pages with some information such as best practises/guides etc. These information will be synced with AWS Kendra , and we can use LLM to produce meaningful guides to users. 
In real world such as big enterprises there will be hundreds (if not thousands) of confluence pages and user can get meaningful results rather from chatbots rather than surfing various pages to filter required information. 

---
## 2 Create AWS Kendra Index & Add Confluence as Data Source

### 2.1 Create AWS Kendra Index. 

Go to AWS Kendra and create an Index. 

![Alt text](<images/Kendra Image 1.png>)

Follow the prompts and complete creation of Index. 

![Alt text](<images/Kendra Image 2.png>)

### 2.2 Add Confluence as Data Source

Once Index is created click on add a data source from your index page. 

![Alt text](<images/Kendra Image 3.png>)

Fillout required details. You need to create a new secret with Confluence admin username (or user that has access to all pages you want to sync) and token that was created in Step 1. 

You also need to define an IAM role becuase Amazon Kendra requires permissions for other services to create this data source

![Alt text](<images/Kendra Image 4.png>)



![Alt text](<images/Kendra Image 5.png>)


![Alt text](<images/Kendra Image 6.png>)


You can set up sync schedule as needed. 


 **_NOTE:_**  Above stpes are detailed in [AWS Documentation - Confluence connector V2.0](https://docs.aws.amazon.com/kendra/latest/dg/data-source-v2-confluence.html)

