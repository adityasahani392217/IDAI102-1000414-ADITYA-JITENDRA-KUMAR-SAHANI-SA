# 🌍 ShopImpact – Conscious Shopping Dashboard

ShopImpact is a Python-based interactive web application built using Streamlit to promote conscious consumerism. The application helps users track their shopping purchases, estimate the environmental (CO₂) impact of those purchases, and encourages eco-friendly behavior through badges, suggestions, and visual feedback. The goal of ShopImpact is to transform sustainability awareness into a simple, engaging, and motivating experience rather than one driven by guilt or complexity.

## 🎯 Project Objective

The objectives of this project are to design and deploy an interactive Python application for social good, apply core Python concepts such as lists, dictionaries, control structures, and functions, build a responsive and user-friendly web interface using Streamlit, encourage ethical and environmentally responsible shopping habits, and reflect on the social and ethical impact of technology solutions.

## 👥 Target Users

The target users for this application include students and young adults, eco-conscious families, and individuals interested in sustainable and mindful living.

## 🧠 Key Features

Compulsory Features:
- Input fields for product type, brand name, and price
- Real-time estimation of CO₂ impact using predefined multipliers
- Monthly dashboard showing total spending and estimated environmental impact
- Eco-friendly badge system to reward low-impact behavior
- Suggested greener alternatives for different product categories
- Turtle graphics used as creative visual rewards

Optional Enhancements:
- Random eco-friendly tips after adding purchases
- Motivational quotes related to sustainable living
- Clean and accessible user interface using earthy color themes

## 🧮 Python Logic Overview

Purchase data is stored using lists of dictionaries. Each purchase record contains the product type, brand name, price, estimated CO₂ impact, and month of purchase. Environmental impact is calculated using the formula: Estimated Impact = Price × Impact Multiplier. Modular functions are used for impact calculation, badge assignment, and dashboard summarization.

Note: CO₂ impact values are estimates intended for awareness purposes only and are not exact scientific measurements.

## 🖥️ Streamlit Interface Design

The user interface is divided into four main sections. The top section contains the purchase input form. The main section displays the monthly impact dashboard with real-time updates. The sidebar shows eco badges and greener alternative suggestions. The bottom section provides eco tips and motivational messages. The interface uses large fonts, clear spacing, and earthy colors such as green and blue to enhance readability and accessibility.

## 🎨 Turtle Graphics Integration

Turtle graphics are used creatively to visualize eco-friendly behavior, such as drawing leaves or badges when users make low-impact purchases. Due to Streamlit’s web-based environment, Turtle drawings are demonstrated through generated visuals and screenshots included in the documentation, fulfilling the creative visualization requirement of the assignment.

## ✅ Testing and Validation

The application was tested using 10–15 sample purchase entries, including high-impact products such as electronics and low-impact products such as second-hand items. Edge cases such as zero or low price values were also tested. All calculations, badge logic, and real-time updates were verified for correctness and usability.

## 🚀 Deployment

The application is deployed using Streamlit Cloud.

Live Application Link:
PASTE YOUR STREAMLIT APP LINK HERE

GitHub Repository Link:
PASTE YOUR GITHUB REPOSITORY LINK HERE

## 🛠️ How to Run the Application Locally

1. Clone the repository using: git clone <your-repository-link>
2. Navigate to the project directory.
3. Install required dependencies using: pip install -r requirements.txt
4. Run the Streamlit app using: streamlit run app.py

## 📁 Repository Structure

app.py  
requirements.txt  
README.md  

## 🌱 Ethical and Social Considerations

ShopImpact is designed to promote sustainability using positive reinforcement rather than guilt-driven messaging. The application encourages gradual improvement, awareness, and empowerment while maintaining transparency about the use of estimated environmental data.

## 📌 Conclusion

ShopImpact demonstrates the complete development lifecycle of a Python-based interactive application—from problem understanding and logic design to deployment and documentation. The project successfully integrates technical skills with social responsibility, creating a meaningful and user-friendly solution for conscious shopping.

## 📚 References

Streamlit Documentation  
Python Official Documentation  
Turtle Graphics Documentation  

Developed as part of the CRS: Artificial Intelligence – Python Programming
