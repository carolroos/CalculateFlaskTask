
from flask import Blueprint, request, redirect, url_for
from flask import current_app               
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyBezdjeZrozb-USWoJRjynk-MqYPthvY6o"       


import geocoder
from helpers import haversine_distance

# Blueprint starts here
api = Blueprint('api',__name__,url_prefix='/api')

@api.route('/location', methods = ['POST'])
def location():
    moscow = geocoder.google('Moscow Ring Road')            
    
    
    address = request.form['address']
    try:                          
        g = geocoder.google(address)
        distance = haversine_distance(moscow.lat,moscow.lng,
                                                g.lat,g.lng)

        if distance < 108.9:                                
            current_app.logger.info('%s is inside Moscow Ring Road, entered as %s',g.address,address)
            return redirect(url_for('Website'))  
        current_app.logger.info('Distance between Moscow Ring Road and %s = %s kilometers, entered as %s',
                                                                                g.address,distance,address)

        return redirect(url_for('Website'))                                                                        
        
    except:
        current_app.logger.error('%s is an Invalid Address',address)
        print("llsa")
        return redirect(url_for('Website'),400)             

    

