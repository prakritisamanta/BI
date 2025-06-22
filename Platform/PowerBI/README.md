# PowerBI

Power BI is a collection of software services, apps, and connectors that work together to turn your unrelated sources of data into coherent, visually immersive, and interactive insights. Your data may be an Excel spreadsheet, or a collection of cloud-based and on-premises hybrid data warehouses. Power BI lets you easily connect to your data sources, visualize and discover what's important, and share that with anyone or everyone you want.

### Parts of Power BI

Power BI consists of several elements that all work together, starting with these three basics:

- A Windows desktop application called <b>Power BI Desktop.</b>
- An online SaaS (Software as a Service) service called the <b>Power BI service.</b>
- <b>Power BI mobile apps</b> for Windows, iOS, and Android devices.

<br>

![image001](https://github.com/user-attachments/assets/28e7aa74-d9c7-4ba6-b494-dc8ad7db735b)

These three elements—Power BI Desktop, the service, and the mobile apps—are designed to let you create, share, and consume business insights in the way that serves you and your role most effectively.

Beyond those three, Power BI also features two other elements:

- <b>Power BI Report Builder</b>, for creating paginated reports to share in the Power BI service. Read more about paginated reports later in this article.
- <b>Power BI Report Server</b>, an on-premises report server where you can publish your Power BI reports, after creating them in Power BI Desktop. Read more about Power BI Report Server later in this article.

<br>

## Power BI Desktop

Power BI Desktop integrates proven Microsoft query engine, data modeling, and visualization technologies. Data analysts and others can create collections of queries, data connections, models, and reports, and easily share them with others. Through the combination of Power BI Desktop and the Power BI service, new insights from the world of data are easier to model, build, share, and extend.

Power BI Desktop centralizes, simplifies, and streamlines what can otherwise be a scattered, disconnected, and arduous process of designing and creating business intelligence repositories and reports. Ready to give it a try? Let's get started.

With Power BI Desktop, you can:

1. Connect to data, including multiple data sources.
2. Shape the data with queries that build insightful, compelling data models.
3. Use the data models to create visualizations and reports.
4. Share your report files for others to leverage, build upon, and share. You can share Power BI Desktop .pbix files like any other files, but the most compelling method is to upload them to the Power BI service.

<br>
From the Welcome screen, you can Get data, see Recent sources, open recent reports, Open other reports, or select other links. Select the close icon to close the Welcome screen.

![image002](https://github.com/user-attachments/assets/3d321462-8847-45a2-aee9-fded9157165d)

Along the left side of Power BI Desktop are icons for the three Power BI Desktop views: Report, Data, and Model, from top to bottom. The current view is indicated by the yellow bar along the left, and you can change views by selecting any of the icons.

![image003](https://github.com/user-attachments/assets/ba5f825a-862f-474c-bc6b-2ee216e1c77c)

![image004](https://github.com/user-attachments/assets/87a3fb93-dc3f-4890-9589-d82152f4af75)

Power BI Desktop also includes the Power Query Editor, which opens in a separate window. In Power Query Editor, you can build queries and transform data, then load the refined data model into Power BI Desktop to create reports.

<br>

### Connect to data

With Power BI Desktop installed, you're ready to connect to the ever-expanding world of data. To see the many types of data sources available, select Get Data > More in the Power BI Desktop Home tab, and in the Get Data window, scroll through the list of All data sources. In this quick tour, you connect to a couple of different Web data sources.

![image005](https://github.com/user-attachments/assets/72f39f88-8ce5-4be3-9484-9aa7b255de0b)

Imagine you're a data analyst working for a sunglasses retailer. You want to help your client target sunglasses sales where the sun shines most frequently. The Bankrate.com Best and worst states for retirement page has interesting data on this subject.

On the Power BI Desktop Home tab, select Get Data > Web to connect to a web data source.

![image006](https://github.com/user-attachments/assets/25b83eee-cbae-4880-b739-1f313279e601)

In the From Web dialog box, paste the address https://www.bankrate.com/retirement/best-and-worst-states-for-retirement/ into the URL field, and select OK.

![image007](https://github.com/user-attachments/assets/db1a8001-1af8-4be0-be32-1719636fc3f3)

If prompted, on the Access Web Content screen, select Connect to use anonymous access.

The query functionality of Power BI Desktop goes to work and contacts the web resource. The Navigator window returns what it found on the web page, in this case an HTML table called Ranking of best and worst states for retirement, and five other suggested tables. You're interested in the HTML table, so select it to see a preview.

At this point you can select Load to load the table, or Transform data to make changes in the table before you load it.

![image008](https://github.com/user-attachments/assets/1ef58a7a-3f07-4ef5-817a-6192e7c27de2)

When you select Transform data, Power Query Editor launches, with a representative view of the table. The Query Settings pane is on the right, or you can always show it by selecting Query Settings on the View tab of Power Query Editor.

![image009](https://github.com/user-attachments/assets/e7d6268e-7b03-489a-b9b0-6533e2c5fca4)

<br>

### Shape data

Now that you're connected to a data source, you can adjust the data to meet your needs. To shape data, you provide Power Query Editor with step-by-step instructions for adjusting the data while loading and presenting it. Shaping doesn't affect the original data source, only this particular view of the data.

![image010](https://github.com/user-attachments/assets/92a620df-9ce1-4772-99ea-40c122915219)

![image011](https://github.com/user-attachments/assets/637ae60b-7e83-4341-9850-63850438d590)

![image012](https://github.com/user-attachments/assets/badb80d8-4fb7-422d-9f79-6142a6a13b44)

![image013](https://github.com/user-attachments/assets/55216fe1-4c52-4fe2-85c9-6e47df9f855d)

![image014](https://github.com/user-attachments/assets/cf4aa83d-0f70-4088-9150-146f25a38d2c)

![image015](https://github.com/user-attachments/assets/3e6838d6-fae4-4835-93fe-264a6a914b77)

![image016](https://github.com/user-attachments/assets/6a96a107-d7be-44dc-8e2c-04a2dfe4f9df)

![image017](https://github.com/user-attachments/assets/f7242d81-b397-4fb1-ba6c-489a3afa02f4)

<br>

### Combine data

The data about various states is interesting, and will be useful for building additional analysis efforts and queries. But there's one problem: most data out there uses two-letter abbreviations for state codes, not the full names of the states. To use that data, you need some way to associate your state names with their abbreviations.

You're in luck. Another public data source does just that, but the data will need a fair amount of shaping before you can combine it with your sunglass table.

To import the state abbreviations data into Power Query Editor, select New Source > Web from the New Query group on the Home tab of the ribbon.

![image018](https://github.com/user-attachments/assets/b9a6ef1f-74d0-4b1f-8cb3-2a490a42183a)

![image019](https://github.com/user-attachments/assets/a09cdce1-84c5-4c9f-92ac-b1c2d48d4ec6)

![image020](https://github.com/user-attachments/assets/5daab617-4009-46a9-853a-d463dcee7815)

![image021](https://github.com/user-attachments/assets/7a31a9cc-8f82-415e-ae7e-3de061530447)

![image022](https://github.com/user-attachments/assets/193ba1c5-cd07-4d0d-a3b7-e28359fab728)

![image023](https://github.com/user-attachments/assets/22af274e-fe72-4e43-86ce-5944f1fcfd7d)

![image024](https://github.com/user-attachments/assets/868d6e1b-cefc-4bd3-8e8f-05c9cd36c5c0)

![image025](https://github.com/user-attachments/assets/52c467b8-53a0-4325-8a22-f17c72dda3d1)

<br>

### Build reports

In Power BI Desktop Report view, you can build visualizations and reports. The Report view has six main areas:

<img width="714" alt="image026" src="https://github.com/user-attachments/assets/eb5ba6d0-9be4-423b-8e60-0cfc1653582f" />

1.	The ribbon at the top, which displays common tasks associated with reports and visualizations.
2.	The canvas area in the middle, where you create and arrange visualizations.
3.	The pages tab area at the bottom, which lets you select or add report pages.
4.	The Filters pane, where you can filter data visualizations.
5.	The Visualizations pane, where you can add, change, or customize visualizations, and apply drillthrough.
6.	The Format pane, where you design the report and visualizations.
7.	The Fields pane, which shows the available fields in your queries. You can drag these fields onto the canvas, the Filters pane, or the Visualizations pane to create or modify visualizations.

You can expand and collapse the Filters, Visualizations, and Fields panes by selecting the arrows at the tops of the panes. Collapsing the panes provides more space on the canvas to build cool visualizations.

<br>
![image027](https://github.com/user-attachments/assets/0b25c00a-a2f8-4463-bcdf-fc480a682dbd)

![image028](https://github.com/user-attachments/assets/9124c5bb-b0b8-428a-8d22-c2ea98c3b7c4)

<img width="161" alt="image029" src="https://github.com/user-attachments/assets/d02088e7-186a-476e-8b75-df214a63ce11" />

<img width="459" alt="image030" src="https://github.com/user-attachments/assets/7e591604-5a07-4d50-9acc-9800eec9e92e" />

<img width="698" alt="image031" src="https://github.com/user-attachments/assets/097eae62-5381-4a78-acbf-9b17336bb5b4" />

<img width="585" alt="image032" src="https://github.com/user-attachments/assets/e272f168-c82f-4a82-91ce-86e8cae6db0a" />

<img width="346" alt="image033" src="https://github.com/user-attachments/assets/24d92498-5b00-4d57-a51b-f1c59e7843a8" />

<img width="584" alt="image034" src="https://github.com/user-attachments/assets/c5ccd537-eef8-49a7-bc94-c4b929a250b3" />

<img width="474" alt="image035" src="https://github.com/user-attachments/assets/2f382322-e5fa-440f-81e0-5952857f6ec9" />

![image036](https://github.com/user-attachments/assets/af20dec7-84e2-4483-b28c-175bf026a8a7)

<img width="711" alt="image037" src="https://github.com/user-attachments/assets/117d9c6c-c677-4680-a746-2087670171c3" />

<br>

### Share your work

Now that you have a Power BI Desktop report, you can share it with others. There are a few ways to share your work. You can distribute the report .pbix file like any other file, you can upload the .pbix file from the Power BI service, or you can publish directly from Power BI Desktop to the Power BI service. You must have a Power BI account to be able to publish or upload reports to Power BI service.

To publish to the Power BI service from Power BI Desktop, from the Home tab of the ribbon, select Publish.

![image038](https://github.com/user-attachments/assets/5df238d6-384c-4c33-9335-c56c80e31771)

![image039](https://github.com/user-attachments/assets/09fcbd9c-6d98-4a33-ad2d-1d5313a946f3)

![image040](https://github.com/user-attachments/assets/36fcfcfe-2494-424d-8ad0-a3930915c080)

![image041](https://github.com/user-attachments/assets/52478fc7-04f4-480d-8c83-6731e1a58397)

![image042](https://github.com/user-attachments/assets/03e3e0bf-da9f-419e-841a-dbd1afe78578)

![image043](https://github.com/user-attachments/assets/55f64a66-5bf7-4dd4-9f40-8d89f4be2287)

![image044](https://github.com/user-attachments/assets/bdf24fec-c02a-4540-8f93-2d16bb2d7f64)

![image045](https://github.com/user-attachments/assets/ecb26be8-2fcd-4974-875e-98dcb6b8653d)

<br>

# Power BI service

This tutorial is an introduction to some of the features of the Power BI service. In it, you connect to data, create a report and a dashboard, and ask questions of your data. You can do much more in the Power BI service; this tutorial is just to whet your appetite. For an understanding of how the Power BI service fits in with the other Power BI offerings, we recommend reading What is Power BI.

Are you a report reader rather than a creator? Getting around in the Power BI service is a good starting place for you.

<img width="641" alt="image046" src="https://github.com/user-attachments/assets/8571cedb-352b-4beb-b6bf-7ccd949f963a" />

In this tutorial, you complete the following steps:

- Sign in to your Power BI online account, or sign up, if you don't have an account yet.
- Open the Power BI service.
- Get some data and open it in report view.
- Use that data to create visualizations and save it as a report.
- Create a dashboard by pinning tiles from the report.
- Add other visualizations to your dashboard by using the Q&A natural-language tool.
- Resize, rearrange, and edit details for the tiles on the dashboard.
- Clean up resources by deleting the dataset, report, and dashboard.

<br>

### Sign up for the Power BI service

![image047](https://github.com/user-attachments/assets/e8b22624-cbff-4a3b-9eab-b47f5774e039)

<br>

### Get data

![image048](https://github.com/user-attachments/assets/b875dc57-c5ed-42b7-9641-1d994ab0ef31)

![image049](https://github.com/user-attachments/assets/1d016813-8c3b-4707-b5be-0cfcad38dd9b)

![image050](https://github.com/user-attachments/assets/562c5e94-3920-4000-a4aa-c8fe2305dd20)

<img width="849" alt="image051" src="https://github.com/user-attachments/assets/86ec7183-4a54-4fad-82a0-6d7730b4ad7d" />

![image052](https://github.com/user-attachments/assets/c6da9c69-50f4-4f6b-879b-b7d265f13155)

![image053](https://github.com/user-attachments/assets/bc66ebaa-f28b-43a0-8678-0b5e326815b4)

<br>

### Create a chart in a report

![image054](https://github.com/user-attachments/assets/4755702b-17eb-4b56-892f-1c480bc1ed28)

![image055](https://github.com/user-attachments/assets/89319478-14a5-4959-8b63-c2006e99e2bb)

<img width="267" alt="image056" src="https://github.com/user-attachments/assets/443846a8-cba3-442d-80c8-6342fbbca0bb" />

![image057](https://github.com/user-attachments/assets/c24f409b-3db6-44c4-9a1b-4b0b9d76c2de)

![MSTR](assets/images/power_bi/image058.png)

![MSTR](assets/images/power_bi/image059.png)

![MSTR](assets/images/power_bi/image060.png)

![MSTR](assets/images/power_bi/image061.png)


<br>

### Explore with Q&A

For a quick exploration of your data, try asking a question in the Q&A question box. Q&A lets you ask natural-language queries about your data. In a dashboard, the Q&A box is at the top (Ask a question about your data) under the menu bar. In a report, it's in the top menu bar (Ask a question)

![MSTR](assets/images/power_bi/image062.png)

![MSTR](assets/images/power_bi/image063.png)

![MSTR](assets/images/power_bi/image064.png)

![MSTR](assets/images/power_bi/image065.png)

![MSTR](assets/images/power_bi/image066.png)

![MSTR](assets/images/power_bi/image067.png)

![MSTR](assets/images/power_bi/image068.png)


<br>

### Reposition tiles

We can rearrange the tiles to make better use of the dashboard space.

![MSTR](assets/images/power_bi/image069.png)

![MSTR](assets/images/power_bi/image070.png)

![MSTR](assets/images/power_bi/image071.png)

![MSTR](assets/images/power_bi/image072.png)

<br>

### Clean up resources

Now that you've finished the tutorial, you can delete the dataset, report, and dashboard.

![MSTR](assets/images/power_bi/image073.png)


<br><br><br>
Source: `https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-getting-started`

<br><br>
