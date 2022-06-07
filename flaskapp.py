from flask import Flask,jsonify,request

app=Flask(__name__)
list=[
    {
        'id':1,
        'name':u'raju',
        'contact':u'1234567890',
        'done':False
    },
    {
        
        'id':2,
        'name':u'rahul',
        'contact':u'1324567890',
        'done':False
    },
]
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'providedata'
        },400)
    
    contact={
          'id':list[-1]['id']+1,
        'name':request.json['name'],
        'contack':request.json.get('contact',''),
        'done':False

    }
    list.append(contact)
    return jsonify({
            'status':'success',
            'message':'contactadded'
        })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data':list
    })
if(__name__=='__main__'):
    app.run()
