# 🌍 ShopImpact – Conscious Shopping Dashboard

ShopImpact is a Python-based interactive web application developed using **Streamlit** with the goal of promoting conscious and environmentally responsible consumer behavior. The application enables users to record their shopping purchases, estimate the associated environmental (CO₂) impact, and understand how everyday buying decisions contribute to climate change. Rather than relying on fear or guilt, ShopImpact focuses on awareness, transparency, and positive reinforcement to motivate gradual and sustainable behavioral change.

In a world where sustainability data often feels abstract or overwhelming, ShopImpact simplifies the concept of environmental impact into clear visuals, scores, and rewards. This approach makes the application suitable for a wide audience, especially students and first-time learners exploring the intersection of technology and social responsibility.

---

## 🎯 Project Objective

The primary objectives of the ShopImpact project are:

- 🌱 To design and deploy an interactive Python application that addresses a real-world social and environmental issue  
- 🧠 To apply fundamental Python programming concepts, including lists, dictionaries, loops, conditionals, and user-defined functions  
- 🖥️ To build a responsive, intuitive, and visually clean web interface using the Streamlit framework  
- ♻️ To encourage users to reflect on their shopping habits and adopt more sustainable alternatives  
- ⚖️ To demonstrate how technology can be used ethically to support awareness, responsibility, and positive social outcomes  

This project aligns technical learning with ethical reflection, fulfilling both educational and social-good objectives.

---

## 👥 Target Users

ShopImpact is designed for a broad but clearly defined audience, including:

- 🎓 Students and young adults learning about sustainability and responsible consumption  
- 👨‍👩‍👧 Eco-conscious families interested in tracking and improving their shopping habits  
- 🌿 Individuals exploring mindful and sustainable living practices  

The application requires no prior technical expertise and is accessible to users of all backgrounds.

---

## 🧠 Key Features

### ✅ Compulsory Features

- 📝 Interactive input form to record purchases with product type, brand name, and price  
- 🌫️ Real-time estimation of CO₂ impact using predefined, category-based multipliers  
- 📊 Monthly dashboard summarizing:
  - Total spending  
  - Estimated environmental impact  
- 🏅 Eco-friendly badge system that rewards low-impact shopping behavior  
- 🌱 Suggested greener alternatives tailored to each product category  
- 🐢 Creative use of Turtle Graphics as symbolic eco rewards (documented representation)

### ⭐ Optional Enhancements

- 💡 Random eco-friendly tips displayed after logging purchases  
- 🌟 Motivational quotes to reinforce positive sustainability messaging  
- 🎨 Clean and accessible user interface using earthy color themes (green and blue)  

---

## 🧮 Python Logic Overview

Purchase information is stored using a **list of dictionaries**, a structure that allows flexible data storage and easy aggregation. Each purchase entry includes the following attributes:

- Product category  
- Brand name  
- Purchase price  
- Estimated CO₂ impact  
- Month of purchase  

The environmental impact is calculated using the formula:
Impact multipliers vary by product category to reflect relative environmental cost. The application uses modular, reusable functions to handle:

- Impact calculation  
- Eco score computation  
- Badge assignment  
- Monthly summaries and comparisons  

⚠️ **Disclaimer:** CO₂ impact values are simplified estimates intended for educational and awareness purposes only. They do not represent precise scientific measurements.

---

## 🖥️ Streamlit Interface Design

The Streamlit interface is divided into four logical sections to improve usability and clarity:

1. **Purchase Input Section** – Allows users to easily log new purchases  
2. **Monthly Dashboard** – Displays real-time calculations of spending and CO₂ impact  
3. **Sidebar Panel** – Shows eco badges and recommended greener alternatives  
4. **Engagement Section** – Presents eco tips and motivational messages  

The layout emphasizes readability through proper spacing, large fonts, and consistent color usage, ensuring accessibility across devices.

---

## 📊 Green Transition Simulation

A key advanced feature of ShopImpact is the **Green Transition Simulation**. This component includes an interactive comparison graph that visually represents:

- 🔴 CO₂ emissions under current shopping practices  
- 🟢 Projected CO₂ emissions after adopting greener alternatives  

Users can adjust a slider to simulate the percentage of purchases shifted toward sustainable options. This feature highlights the tangible benefits of conscious decision-making and encourages experimentation with sustainability scenarios.

---

## 🎨 Turtle Graphics Integration

Turtle graphics are used creatively to symbolize eco-friendly behavior, such as drawing leaves, symbols, or celebratory visuals when users achieve low-impact milestones. Due to Streamlit’s web-based execution environment, direct Turtle animations are represented through documented visuals and screenshots included in the project documentation. This approach satisfies the creative visualization requirement of the assignment.

---

## ✅ Testing and Validation

The application was tested using approximately 10–15 sample purchase records, including:

- ⚡ High-impact categories such as electronics  
- 🌱 Low-impact categories such as second-hand goods  

Edge cases such as zero-price or very low-price inputs were also tested. All calculations, badge logic, and real-time dashboard updates were verified to ensure accuracy, stability, and usability.

---

## 🚀 Deployment

The application is deployed using **Streamlit Cloud**, allowing public access through a web browser without local setup.

🔗 **Live Application Link:**  
https://idai102-1000414-aditya-jitendra-kumar-sahani-shopimpact.streamlit.app/

---

## 🛠️ How to Run the Application Locally

1. Clone the repository: git clone 

2. Navigate to the project directory: cd ShopImpact

3. Install the required dependencies: pip install -r requirements.txt

4. Run the Streamlit application: streamlit run app.py

---

## 📁 Repository Structure

ShopImpact/  
├── app.py  
├── requirements.txt  
└── README.md  

---

## 🌱 Ethical and Social Considerations

ShopImpact is designed with ethical responsibility at its core. The application avoids fear-based messaging and instead promotes sustainability through encouragement, awareness, and empowerment. Transparency is maintained regarding the use of estimated data, and users are encouraged to view sustainability as a gradual, achievable journey rather than an all-or-nothing goal.

---

## 📌 Conclusion

ShopImpact demonstrates the complete development lifecycle of a Python-based interactive application—from problem identification and logic design to deployment and detailed documentation. By combining technical implementation with ethical intent, the project highlights how software solutions can meaningfully contribute to social good and environmental awareness.

---

## 📚 References

📘 Streamlit Documentation  
🐍 Python Official Documentation  
🐢 Turtle Graphics Documentation  

Developed as part of the **CRS: Artificial Intelligence – Python Programming**
