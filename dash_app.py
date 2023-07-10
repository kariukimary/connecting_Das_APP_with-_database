from dash import Dash, html,dcc,Input,Output,callback
import mysql
from mysql.connector import connect
from PIL import Image
#import base64


#database details
host='localhost'
user='root'
password='chatme@2023'
database='mydb'
    
#connect to mysql databases
conn=connect(
    host=host,
    user=user,
    password=password,
    database=database)

#query the images table
cursor=conn.cursor()
cursor.execute('SELECT * FROM images')
images=cursor.fetchall


#using direct image file path
image_path='C:\\Users\\Admin\\Desktop\\DSAIL\\assets\\puppy3.jpg'

#using pillow to read the image
pil_img=Image.open('C:\\Users\\Admin\\Desktop\\DSAIL\\assets\\puppy3.jpg')


#intialize the app
app=Dash(__name__)

#app layout
app.layout=html.Div([html.H1(" DASH ",style={'text-align':'center','color':'blue'}),
                     html.H2('dash puppies',style={'color':'red'}),
                     html.Img(src=pil_img),
                     html.Br(),
                     html.Br(),
                     html.Div([
                         html.Label("first feature"),
                         dcc.Dropdown(["long ears","short ears","medim nose","wide eyes","tiny eyes","short legs"],
                         value='long ears',
                         #multi=True,
                         id="feature_one"),
                         
                         
                         html.Br(),
                         html.Label("second feature"),
                         dcc.Dropdown(["long ears","short ears","medim nose","long legs","tiny eyes","short legs"],
                         value='short legs',
                         #multi=True,
                         id="feature_two"),
                         
                         html.Br(),
                         html.Label("third feature"),
                         dcc.Dropdown(["long ears","short ears","medim nose","tiny eyes","short legs"],
                         value='medim nose',
                         #multi=True,
                         id="feature_three"),
                         
                         html.Br(),
                         html.Button('SAVE',id='save-button',n_clicks=0),
                         
                         html.Div(id='database', children = [])
                        
                     ]),
                    
])

@callback(
    Output('database', 'children'),
    [Input('feature_one', 'value'),
     Input('feature_two', 'value'),
     Input('feature_three', 'value'),
     Input('save-button', 'n_clicks')
           ]
)

def save_database(feature_one, feature_two, feature_three, n_clicks):
    if n_clicks >= 1:
        conn = mysql.connector.connect(host=host,user=user,password=password,database=database)
        cursor = conn.cursor()
        
        add_ = """INSERT INTO images3
        (filename,feature_one, feature_two, feature_three)
        VALUES(%s, %s, %s, %s)"""
        
        filename = "puppy"
        values = (str((filename)),feature_one, feature_two, feature_three)
        
        cursor.execute(add_,values)
        
        print("Data saved!")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        
        




    

#running the app
if __name__=='__main__':
    app.run_server(debug=True)

