import pickle
import streamlit as st


st.sidebar.header(' Prediction Classification Penguins')
#import the data


st.title(" Prediction App classifier penguins")

# loading the trained model
pickle_in = open('classifier_penguins.pkl', 'rb') 
classifier = pickle.load(pickle_in)

#st.subheader('Data Information:')

@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
#Culmen_Length, Culmen_Depth]
def prediction(Culmen_Length, Culmen_Depth):   
    
    # Making predictions 
    prediction = classifier.predict( 
        [[Culmen_Length, Culmen_Depth]])
     
    if prediction == 0:
        pred = 'Adelie'
    if prediction == 1:
        pred = 'Gentoo'
    if prediction == 2:
        pred = 'Chinstrap'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#5b8a72;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit classifier penguins Prediction ML App</h1> 
    </div> 
    """
    #chart = st.bar_chart(pickle_in)  
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    #Culmen_Length, Culmen_Depth
     
    #Estrato = st.number_input("Estrato")
    #Estrato = float(Estrato)
    
    Culmen_Length = st.sidebar.slider("Culmen Length (mm)", float(32.100000), float(59.600000), float(25.0), float(1.0))
    
    Culmen_Depth = st.sidebar.slider("Culmen Depth (mm)", float(13.100000), float(21.500000), float(18), float(1.0))
    
    result =""
    
    html_temp1 = """ 
    <div padding:23px"> 
     
    </div> 
    """
    #chart = st.bar_chart(pickle_in)  
    # display the front end aspect
    st.markdown(html_temp1, unsafe_allow_html = True) 
    
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Culmen_Length, Culmen_Depth) 
        st.success('El resultado es: {}'.format(result))
       
     
if __name__=='__main__': 
    main()