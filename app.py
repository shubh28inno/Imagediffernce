from flask import Flask, request
import uuid

app= Flask(__name__)

items={
      "213dbf9421ea42f094cbe1af0de17231":{
                                         "name":"Green mojito",
                                         "price":"38"
     },
      "41a3600dfbe1479381d5e0f1ed892e9c":{
                                         "name": " samosa",
                                         "price":"20"
                                         }
}

@app.get('/get-items')
def get_items():
    return {"item":items}

# @app.get('/get-item/<string:name>')
@app.get('/get-item')
def get_item():
    id=request.args.get('id')
    try:
        return items[id]
    except KeyError:
        return {'message':"Record doesn't match"}
# @app.get('/get-item')
# def get_item():
#     name=request.args.get('name')
#     for item in items:
#         if name == item['name']:
#            return item
#     return {'message':"Record doesn't match"}

@app.post('/add-items')
def add_items():
    items[uuid.uuid4().hex]=request.get_json()
    return {"message":"item added succesfully"}
# @app.post('/add-items')
# def add_items():
#     request_data=request.get_json()
#     items.append(request_data)
#     return {"message":"item added succesfully"}

@app.put('/update-items')
def update_items():
    id=request.args.get('id')
    if id in items.keys():
            items[id]=request.get_json()
            return {"message":"item updated succesfully"}
    else:
        return {"message":"item did'nt updated succesfully"}
# @app.put('/update-items')
# def update_items():
#     request_data=request.get_json()
#     for item in items:
#         if item['name']==request_data['name']:
#             item['price']=request_data['price']
#             return {"message":"item updated succesfully"}
#     return {"message":"item did'nt updated succesfully"}

@app.delete('/delete-item')
def delete_item():
    id=request.args.get('id')
    if id in items.keys():
        del items[id]
        return {'message':"item deleted successfully"}
    else: 
        return {'message':"Record doesn't match"}
# @app.delete('/delete-item')
# def delete_item():
#     name=request.args.get('name')
#     for item in items:
#         if name == item['name']:
#            items.remove(item)
#            return {'message':"item deleted successfully"}
#     return {'message':"Record doesn't match"}