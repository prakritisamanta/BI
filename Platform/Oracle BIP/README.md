# What is Oracle BI Publisher (BIP)?

**Oracle Business Intelligence Publisher (BIP)** is an enterprise reporting solution from Oracle, primarily designed for creating and managing highly formatted, pixel-perfect reports, forms, and documents. While it can be used standalone, it's most commonly integrated with other Oracle products, especially **Oracle Fusion Applications** (e.g., Fusion ERP, HCM, SCM) where it serves as the core engine for operational reporting and document generation.

## Key Characteristics and Features:

1.  **Pixel-Perfect Reporting:**
    * BIP excels at generating documents that require precise formatting, adherence to branding guidelines, and specific layouts (e.g., invoices, purchase orders, checks, financial statements, shipping labels).
    * This distinguishes it from more analytical BI tools (like Tableau or Power BI) that focus on interactive dashboards and data exploration.

2.  **Separation of Concerns (Data, Layout, Translation):**
    * This is a foundational principle of BIP, promoting reusability and efficiency.
    * **Data Model:** Defines how data is extracted from various sources (databases, web services, XML files, Oracle Fusion Applications, etc.) and delivered as XML.
    * **Layout/Template:** Specifies the visual design of the report. This is where you apply branding, fonts, colors, and structure. Common template types include:
        * **RTF (Rich Text Format):** Created in Microsoft Word using the BI Publisher Desktop Add-in. Highly popular for its ease of use for business users.
        * **PDF:** For designing forms using Adobe Acrobat.
        * **Excel:** For Excel-based templates.
        * **Flash, HTML, XSL-FO:** For various other use cases.
    * **Translation:** Allows a single report template to be rendered in multiple languages by applying language-specific translations.

3.  **Versatile Output Formats:**
    * BIP can generate reports in a wide range of formats to suit different needs:
        * **PDF (most common)**
        * **HTML** (for web viewing)
        * **Microsoft Excel (XLS, XLSX)**
        * **RTF**
        * **CSV**
        * **XML**
        * **Microsoft PowerPoint**
        * **Flash**

4.  **Flexible Data Sources:**
    * It can connect to almost any data source imaginable:
        * Oracle Fusion Cloud Applications (ERP, HCM, SCM, CRM)
        * Relational Databases (Oracle Database, SQL Server, MySQL, etc.)
        * Web Services
        * XML Files
        * Flat Files (CSV)
        * LDAP servers
        * Other BI Servers (e.g., Oracle BI Enterprise Edition - OBIEE)

5.  **Scheduling and Bursting:**
    * **Scheduling:** Enables reports to be run automatically at predefined intervals (e.g., hourly, daily, weekly, monthly) or based on custom triggers.
    * **Bursting:** A powerful feature to generate a single report and then split it into multiple, individualized documents based on a key. For example, sending unique invoices to 1,000 customers from a single report run, or delivering individual pay stubs to employees.

6.  **Automated Delivery Options:**
    * Reports can be automatically distributed to various destinations:
        * **Email**
        * **Printer**
        * **Fax**
        * **FTP/SFTP**
        * **WebDAV**
        * **Oracle Content Management (formerly Oracle WebCenter Content)**
        * Custom delivery channels

7.  **Security and Governance:**
    * Offers robust security features to control access to reports and data:
        * Role-based access control.
        * Integration with enterprise security models (e.g., Oracle Identity Management).
        * Password protection for PDF output.
        * Digital signatures for PDF documents.
        * Data encryption for sensitive outputs.

## Integration with Oracle Fusion Applications:

For users of Oracle's Cloud ERP, HCM, SCM, and CRM suites (collectively known as Oracle Fusion Applications), BIP is the **native and primary reporting tool** for generating operational reports, transactional documents (like invoices, purchase orders, statements), and customer-facing documents. Most standard reports delivered with Fusion Applications are built using BIP, and it's the go-to tool for creating custom operational reports within that ecosystem.

## Evolution and Current Naming:

While still widely known as "BI Publisher" or "BIP," especially in the context of Oracle Fusion Applications, Oracle has been evolving its analytics offerings. The functionality of BI Publisher is now often referred to as **Oracle Analytics Publisher** and is a component of the broader **Oracle Analytics Cloud (OAC)** suite. For new developments and a more comprehensive analytics platform, Oracle typically promotes OAC, which integrates data visualization, self-service BI, and advanced analytics alongside the traditional pixel-perfect reporting capabilities inherited from BIP. However, the core underlying technology and principles of "Publisher" remain consistent.
