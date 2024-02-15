import streamlit as st


col1, col2 = st.columns(2)

with col1:
   st.title('Hey There 👋')
   st.header("I'm Difa Fisabilillah")
   st.markdown("Welcome to my gateway into the world of data! On my journey, I have gathered valuable experiences and projects to expertise in data exploration, and dedication to becoming a high-caliber data analyst, data scientist, and business intelligence professional. I believe that every piece of data has a story, and I am excited to collaboratively write new success stories to further explore the potential of data.")

with col2:
   st.image("./image/Group 4.png")
   
tab1, tab2, tab3 = st.tabs(["About Me", "See My Portofolio", "Certification"])

with tab1:
   st.header("Skills")

   col1, col2, col3, col4= st.columns(4)
   
   with col1:
    
    
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 30px;
            width: 250px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>Python</p>
            <img src="https://pluspng.com/img-png/python-logo-png-open-2000.png" alt="Python Image">
            
        </div>
    """,unsafe_allow_html=True
)

   with col2:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>SQL</p>
            <img src="https://dirceuresende.com/wp-content/uploads/2018/01/Azure-SQL-Database-generic_COLOR.png" alt="SQL Image">
            
        </div>
    """,unsafe_allow_html=True
)
    
   with col3:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>Excel</p>
            <img src="https://logodownload.org/wp-content/uploads/2020/04/excel-logo-0.png" alt="Excel Image">
            
        </div>
    """,unsafe_allow_html=True
)
   

   with col4:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
            <p>Tableau</p>
            <img src="https://promto.com/wp-content/uploads/2019/08/icon-tableau-1.png" alt="tableau Image">
            
        </div>
    """,unsafe_allow_html=True
)


   col5, col6, col7, col8= st.columns(4)
   
   with col5:
    
    
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 30px;
            width: 250px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>Jupyter Notebook</p>
            <img src="https://mickaellalande.github.io/post/tutorial/how-to-install-jupyter-notebook-on-a-server/featured.jpg" alt="Python Image">
            
        </div>
    """,unsafe_allow_html=True
)

   with col6:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>SQL Server</p>
            <img src="https://secureservercdn.net/198.71.233.167/e2d.964.myftpupload.com/wp-content/uploads/2022/01/SSMS_Logo.jpg" alt="SQL Image">
            
        </div>
    """,unsafe_allow_html=True
)
    
   with col7:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
             <p>Google Colab</p>
             

        <img src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Excel Image">
            
        </div>
    """,unsafe_allow_html=True
)
   

   with col8:
    # Menambahkan HTML dan CSS untuk tata letak
    st.markdown(
    """
        <style>
            .custom-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(211, 211, 211, 0.4); /* Warna abu-abu untuk background */
            padding: 15px;
            width: 150px; /* Sesuaikan lebar container sesuai kebutuhan */
            text-align: center; /* Rata tengah keterangan */
            border-radius: 8px; /* Buletkan sudut container */
        }
        .custom-container img {
            width: 50%; /* Agar gambar memenuhi lebar container */
            border-radius: 8px; /* Buletkan sudut gambar */
            margin-bottom: 10px; /* Jarak antara gambar dan keterangan */
        }
        </style>
    """
    , unsafe_allow_html=True)

# Menampilkan container berbentuk kotak dengan gambar dan keterangan
    st.markdown(
    """
        <div class="custom-container">
            <p>Git</p>
            <img src="https://creazilla-store.fra1.digitaloceanspaces.com/icons/3253808/git-icon-icon-md.png" alt="tableu Image">
            
        </div>
    """,unsafe_allow_html=True
)




   st.header(" ")

   st.header("Project Experiences")
   st.markdown("""<style>.col-green {background-color: green;padding: 10px;border-radius: 8px;}</style> 
               """,unsafe_allow_html=True)
   # Membagi layout menjadi dua kolom
   col1, col2 = st.columns(2)
   with col1:
    
    st.markdown("<blockquote><p style='font-size:19px;'>📌 <b>Final Project Python For Data Science</b></p></blockquote>", unsafe_allow_html=True)



   with col2:
    st.markdown('<div class="col-green"> Studi Independent Hacktiv8', unsafe_allow_html=True)
    st.subheader(" ")
   
    st.markdown('''During the five-month independent program for Data Science students at Hacktiv8 Indonesia, which was conducted between August and December 2023 through the Kampus Merdeka platform, I had the chance to work on both individual and group assignments. This provided me with a comprehensive learning experience in data science. 

My  assignments included the following:
<ul><li>📊 Assignment 1: Advanced Visualization</li>
<li>📈 Assignment 2: Descriptive and Inferential Statistics</li>
<li>🧩 Assignment 3: Classification</li>
</ul>

I also worked on some group projects for build Machine Learning Model:
<ul><li>🚖 Final Project 1: Linear & Polynomial Regressions for Predicting Uber & Lyft Prices</li>
<li>🌧 Final Project 2: Logistic Regression & SVM for Rain Prediction</li>
<li>❤️ Final Project 3: Ensemble Classification for Predicting Patient Safety from Heart Disease
<li>💳 Final Project 4: Clustering Credit Card Customers</li>
</ul>
''', unsafe_allow_html=True)


# Membagi layout untuk dua kolom di bawahnya
   col3, col4 = st.columns(2)
   
   with col3:
    
     
     st.markdown("<blockquote><p style='font-size:19px;'>📌 <b>Final Project SQL & Python Portofolio</b></p></blockquote>", unsafe_allow_html=True)

   with col4:
    st.markdown('<div class="col-green"> Project-Based Virtual Intern Data Engineer Kalbe Nutritionals', unsafe_allow_html=True)
    st.subheader(" ")

    st.markdown(''' Finishing various task related with the activity of Data Engineers from Kalbe Nutritionals, such as Data Analysis and Modeling, Data Warehouse, Data Pre Processing, ETL and ELT.
        <ul>
               <li>🛠️ Craft a bash script with meticulous checks to confirm the presence of a directory within a specified path </il>
               <li> 🚀 Checks for verification of the target directory's existence in the designated path  </il>
               <li> 🐍🔧 integrate Python with MySQL to orchestrate  data insertion </il>
               <li> 📊 Convert instruction into SQL Query Language. </il>
               <li> ⭐ Create simple star schema. </il></ul>

''', unsafe_allow_html=True)
    
   col5, col6 = st.columns(2)

   with col5:
    st.markdown("<blockquote><p style='font-size:19px;'>📌 <b>SQL Udemy Course Analysis</b></p></blockquote>", unsafe_allow_html=True)
   with col6:
    st.markdown('<div class="col-green"> SQL Portofolio', unsafe_allow_html=True)
    st.subheader(" ")

    st.markdown(''' Explore the Udemy course data source from 2011-2017 to understand trends that drive subscriber interest in courses offered by Udemy. 
        <ul>
                <li> 🔄 Data Retrieval and Transformation: Extract and modify data using SQL SELECT and transformation functions.  </il>
               <li> 📊 Aggregation and Grouping: Aggregate with SUM, AVG, and group data for a comprehensive understanding. 
 </il>
               <li> 🔍🔠 Joining, Filtering, and Sorting: Combine, filter, and sort datasets for enriched and ordered information. </il>
               <li>📈 Statistical Analysis and Exploration: Use SQL functions for insights and explore data distributions. </il>
               <li> 🚀📄 Optimization and Documentation: Ensure optimal queries, consider indexing, and document steps for reporting. </il></ul>

''', unsafe_allow_html=True)
    
   col7, col8 = st.columns(2)
   with col7:
    st.markdown("<blockquote><p style='font-size:19px;'>📌 <b> Data Visualization & Dashboard Superstore</b></p></blockquote>", unsafe_allow_html=True)
   with col8:
    st.markdown('<div class="col-green"> Excel Portofolio', unsafe_allow_html=True)
    st.subheader(" ")

    st.markdown('''  Identify patterns and trends in sales data and understand customer behavior from superstore data 2016-2020 
        <ul>
                <li>Data Preparation: Import, clean, and organize data effectively.  </il>
               <li> Analysis and Visualization:Utilize PivotTables, charts, and graphs for insightful data exploration.</il>
               <li> Formulas and Calculations: Apply Excel formulas for calculations and statistical analyses. </il>
               <li>Data Filtering and Sorting: Use filters and sorting functions to highlight relevant information.</il>
               <li> Data Validation and Quality Checks: Ensure data accuracy and consistency through validation processes.</il></ul>

''', unsafe_allow_html=True)


   






with tab2:

   st.header("My Portofolio")

    st.image('./image/211.png', caption='Dashboard Udemy using Tableau')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://public.tableau.com/views/Udemy_course_17078732930430/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link'>Dashboard Udemy Course Analysis</a></div>", unsafe_allow_html=True)
    st.header(" ")
   
   col1, col2 = st.columns(2)
   with col1:
    st.image('./image/1.png', caption='SQL Portofolio')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://sql-udemy-course-analysis.streamlit.app/' target='_blank'>SQL Udemy Course Analysis</a></div>", unsafe_allow_html=True)
    st.header(" ")

   with col2:
    st.image('./image/2.png', caption='Uber Lyft Web App Portofolio')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://uber-lyft-price-prediction.streamlit.app/' target='_blank'>Predicting Uber & Lyft Prices</a></div>", unsafe_allow_html=True)
    st.header(" ")
   

   col3, col4 = st.columns(2)
   with col3:
    st.image('./image/3.png', caption='Web App Rain Pradiction')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://rain-classify-in-australia.streamlit.app/' target='_blank'>Rain Prediction</a></div>", unsafe_allow_html=True)
    st.header(" ")

   with col4:
    st.image('./image/4.png', caption='Web App Clustering')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://clustering-credit-card.streamlit.app/' target='_blank'>Clustering Credit Card Customers</a></div>", unsafe_allow_html=True)
    st.header(" ")


   col5, col6 = st.columns(2)
   with col5:
    st.image('./image/5.png', caption='Uber Lyft Notebook')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://colab.research.google.com/drive/1DlBEYAfh0Qiq_qtPDX0AMG4TrD7ujzyp?usp=sharing' target='_blank'>Predicting Uber & Lyft Prices Notebook</a></div>", unsafe_allow_html=True)
    st.header(" ")

   with col6:
    st.image('./image/6.png', caption='Rain Pradiction Notebook')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://colab.research.google.com/drive/1FY1fObs4Tu4E-cME9GHJNxJTh2OFW7oW?usp=sharing' target='_blank'>Rain Prediction Notebook</a></div>", unsafe_allow_html=True)
    st.header(" ")



   col7, col8 = st.columns(2)
   with col7:
    st.image('./image/7.png', caption='Predicting Heart Disease')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://colab.research.google.com/drive/1DlBEYAfh0Qiq_qtPDX0AMG4TrD7ujzyp?usp=sharing' target='_blank'>Predicting Heart Disease Notebook</a></div>", unsafe_allow_html=True)
    st.header(" ")
 
   with col8:
    st.image('./image/8.png', caption='Clustering Credit Notebook')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://colab.research.google.com/drive/1Is8LdhVsTwNjiZi4X5T_X9KesbwB_7dx?usp=sharing' target='_blank'>Clustering Credit Card Customers Notebook</a></div>", unsafe_allow_html=True)
    st.header(" ")


   col9, col10 = st.columns(2)
   with col9:
    st.image('./image/9.png', caption='Final Project SQL & Python')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://docs.google.com/presentation/d/12azDT_ysDqJdzYt8Zt_yFWpih61l2JtQ/edit#slide=id.p3' target='_blank'>Project-Based Virtual Intern Data Engineer Kalbe Nutritionals</a></div>", unsafe_allow_html=True)
    st.header(" ")
 
   with col10:
    st.image('./image/Screenshot 2024-02-14 092552.png', caption='Excel Portofolio')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://docs.google.com/presentation/d/1K4glJTW5WIfZ5Ilu_C_UUbUAvGN7G9aX/edit#slide=id.p2' target='_blank'>Data Visualization & Dashboard Superstore</a></div>", unsafe_allow_html=True)
    st.header(" ")


with tab3:

   st.header("Hacktiv8 Certification")
   
   col1, col2 = st.columns(2)
   with col1:
    st.image('./image/12.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://drive.google.com/file/d/1yLi4FwxGllZfXDl4n6GfDBsFjySie8Kh/view' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")

   with col2:
    st.image('./image/13.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://sertiva.id/credential/f39c8ccd-fc72-4f38-978e-3ea905873383' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")
   

   col3, col4 = st.columns(2)
   with col3:
    st.image('./image/14.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://sertiva.id/credential/cc329ce3-7856-426d-9aee-0c0900ae6255' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")

   with col4:
    st.image('./image/15.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://sertiva.id/credential/d5e4fcd3-6060-41c7-97ff-18dbf83e4955#verify' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")


   col5, col6 = st.columns(2)
   with col5:
    st.image('./image/16.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://sertiva.id/credential/f5df238b-367a-447b-9a03-5b8814ec3125' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")

   


   st.header("Kalbe Nutritionals x Rakamin Academy")
   col7, col8 = st.columns(2)
 
   with col7:
    st.image('./image/17.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://drive.google.com/file/d/1CwpDrnM06qr9oZ1PGmm8eOQ1_a8vRBxR/view?pli=1' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")
 
   with col8:
    st.image('./image/18.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://drive.google.com/file/d/1KYLx8uvBVTf_l8bgYs-TbMUDSaSgVLUr/view' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")

   st.header('Dicoding')
   col9, col10 = st.columns(2)

   with col9:
    st.image('./image/19.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://www.dicoding.com/certificates/2VX364JKQXYQ' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")
 
   with col10:
    st.image('./image/20.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://www.dicoding.com/certificates/KEXL0WDVWPG2' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")

   st.header('Workshop Tableau Pesta Data Nasional')
   col9, col10 = st.columns(2)
   col21, col22= st.columns(2)
   with col21:
    st.image('./image/21.png')

    # Center the text using markdown and CSS
    centered_text_style = """
        display: flex;
        justify-content: center;
    """
    st.markdown(f"<div style='{centered_text_style}'><a href='https://drive.google.com/file/d/1Rqu4CsW1x76ZjtmwJYhZFmfBFIhg0k_z/view?usp=drive_link' target='_blank'>Click to See</a></div>", unsafe_allow_html=True)
    st.header(" ")
 
   with col22:
    
    st.header(" ")
