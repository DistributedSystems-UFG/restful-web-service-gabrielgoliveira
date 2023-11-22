#
# The original code for this example is credited to S. Subramanian,
# from this post on DZone: https://dzone.com/articles/restful-web-services-with-python-flask
#

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Arício Segundo',
 'title':'Technical Leader',
 'salary': '2000'
 },
 {
 'id':'201',
 'name':'Geraldo Rusmão',
 'title':'Sr Software Engineer',
 'salary': '3000'
 }
 ]

# ---------- Meus endpoints ---------

@app.route('/empdb/employee/increase-salary/<empId>',methods=['PUT'])
def updateEmpIncreaseSalary(empId):
    # incrementa o salario do funcionario sendo emp[0]['salary'] += aumento no sentido de aumento

    emp = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(emp) == 0 :
        print('Usuario nao econtrado')
        return jsonify({'err': 'Usuário não encontrado'})
   
    emp[0]['salary'] = float(emp[0]['salary']) + float(request.json['increase'])

    return jsonify(emp)

@app.route('/empdb/employee/average-salary',methods=['GET'])
def getAverageSalarys():
    # calcula a media dos salarios

    average = 0.0
    salarios = [float(pessoa['salary']) for pessoa in empDB if 'salary' in pessoa]

    if len(salarios) > 0 :
        average = sum(salarios)/len(salarios)

    return jsonify({'average' : average})

@app.route('/empdb/employee/get-max-salary',methods=['GET'])
def getMaxSalary():
    # calcula o maior dos salarios
    salarios = [float(pessoa['salary']) for pessoa in empDB if 'salary' in pessoa]
    return jsonify({'salary' : max(salarios)})

# -----------------------------------
@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})


@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):

    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        if 'name' in request.json : 
            em[0]['name'] = request.json['name']

        if 'title' in request.json:
            em[0]['title'] = request.json['title']

    return jsonify(em)

@app.route('/empdb/employee/<empId>/<empSal>',methods=['PUT'])
def updateEmpSal(empId,empSal):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    em[0]['salary'] = empSal
    return jsonify(em)
   
@app.route('/empdb/employee',methods=['POST'])
def createEmp():

    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        empDB.remove(em[0])
        return jsonify({'response':'Success'})
    else:
        return jsonify({'response':'Failure'})

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
