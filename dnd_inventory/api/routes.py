from urllib import response
from flask import Blueprint, request, jsonify
from dnd_inventory.helpers import token_required
from dnd_inventory.models import db, User, Character, Skills, Stats, Classes, Subclasses, character_schema, characters_schema, skills_schema, multi_skills_schema, stats_schema, multi_stats_schema, classes_schema, multi_classes_schema, subclasses_schema, multi_subclasses_schema

api = Blueprint('api',__name__,url_prefix='/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return {'some':'value'}

# Create
@api.route('/character', methods = ['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    stats = request.json['stats']
    classes = request.json['classes']
    race = request.json['race']
    subrace = request.json['subrace']
    background = request.json['background']
    skills = request.json['skills']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")
    character = Character(name, stats, classes, race, subrace, background, skills, user_token=user_token)
    db.session.add(character)
    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)


@api.route('/stats', methods = ['POST'])
@token_required
def create_stats(current_user_token):
    str = request.json['str']
    dex = request.json['dex']
    con = request.json['con']
    int = request.json['int']
    wis = request.json['wis']
    cha = request.json['cha']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")
    stats = Stats(str, dex, con, int, wis, cha, user_token)
    db.session.add(stats)
    db.session.commit()
    response = stats_schema.dump(stats)
    return jsonify(response)

@api.route('/classes', methods = ['POST'])
@token_required
def create_classes(current_user_token):
    art = request.json['art'] 
    barb = request.json['barb']
    bard = request.json['bard']
    cle = request.json['cle']
    dru = request.json['dru']
    fig = request.json['fig']
    mon = request.json['mon']
    pal = request.json['pal']
    ran = request.json['ran']
    rog = request.json['rog']
    sor = request.json['sor']
    war = request.json['war']
    wiz = request.json['wiz']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")
    classes = Classes(art, barb, bard, cle, dru, fig, mon, pal, ran, rog, sor, war, wiz, user_token)
    db.session.add(classes)
    db.session.commit()
    response = classes_schema.dump(classes)
    return jsonify(response)

@api.route('/subclasses', methods = ['POST'])
@token_required
def create_subclasses(current_user_token):
    art = request.json['art'] 
    barb = request.json['barb']
    bard = request.json['bard']
    cle = request.json['cle']
    dru = request.json['dru']
    fig = request.json['fig']
    mon = request.json['mon']
    pal = request.json['pal']
    ran = request.json['ran']
    rog = request.json['rog']
    sor = request.json['sor']
    war = request.json['war']
    wiz = request.json['wiz']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")
    subclasses = Subclasses(art, barb, bard, cle, dru, fig, mon, pal, ran, rog, sor, war, wiz, user_token)
    db.session.add(subclasses)
    db.session.commit()
    response = subclasses_schema.dump(subclasses)
    return jsonify(response)


@api.route('/skills', methods = ['POST'])
@token_required
def create_skills(current_user_token):
    arc = request.json['arc']
    ani = request.json['ani']
    ath = request.json['ath']
    dec = request.json['dec']
    his = request.json['his']
    ins = request.json['ins']
    inti = request.json['inti']
    inv = request.json['inv']
    med = request.json['med']
    nat = request.json['nat']
    perc = request.json['perc']
    perf = request.json['perf']
    pers = request.json['pers']
    rel = request.json['rel']
    soh = request.json['soh']
    ste = request.json['ste']
    sur = request.json['sur']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")
    skills = Skills(user_token, ani, arc, ath, dec, his, ins, inti, inv, med, nat, perc, perf, pers, rel, soh, ste, sur)
    db.session.add(skills)
    db.session.commit()
    response = skills_schema.dump(skills)
    return jsonify(response)


# Retrieve (All from User)
@api.route('/character', methods = ['GET'])
@token_required
def get_all_characters(current_user_token):
    owner = current_user_token.token
    characters = Character.query.filter_by(user_token=owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)

@api.route('/stats', methods = ['GET'])
@token_required
def get_all_stats(current_user_token):
    owner = current_user_token.token
    stats = Stats.query.filter_by(user_token=owner).all()
    response = multi_stats_schema.dump(stats)
    return jsonify(response)

@api.route('/classes', methods = ['GET'])
@token_required
def get_all_classes(current_user_token):
    owner = current_user_token.token
    classes = Classes.query.filter_by(user_token=owner).all()
    response = multi_classes_schema.dump(classes)
    return jsonify(response)

@api.route('/subclasses', methods = ['GET'])
@token_required
def get_all_subclasses(current_user_token):
    owner = current_user_token.token
    subclasses = Subclasses.query.filter_by(user_token=owner).all()
    response = multi_subclasses_schema.dump(subclasses)
    return jsonify(response)

@api.route('/skills', methods = ['GET'])
@token_required
def get_all_skills(current_user_token):
    owner = current_user_token.token
    skills = Skills.query.filter_by(user_token=owner).all()
    response = multi_skills_schema.dump(skills)
    return jsonify(response)



# Retrieve (Single)
@api.route('/character/<id>', methods = ['GET'])
@token_required
def get_character(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        character = Character.query.get(id)
        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401

@api.route('/stats/<id>', methods = ['GET'])
@token_required
def get_stats(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        stats = Stats.query.get(id)
        response = stats_schema.dump(stats)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401

@api.route('/classes/<id>', methods = ['GET'])
@token_required
def get_classes(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        classes = Classes.query.get(id)
        response = classes_schema.dump(classes)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401

@api.route('/subclasses/<id>', methods = ['GET'])
@token_required
def get_subclasses(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        subclasses = Subclasses.query.get(id)
        response = subclasses_schema.dump(subclasses)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401

@api.route('/skills/<id>', methods = ['GET'])
@token_required
def get_skills(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        skills = Skills.query.get(id)
        response = skills_schema.dump(skills)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401



# Update
@api.route('/character/<id>', methods = ['POST','PUT'])
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id)

    character.name = request.json['name']
    character.stats = request.json['stats']
    character.classes = request.json['classes']
    character.race = request.json['race']
    character.subrace = request.json['subrace']
    character.background = request.json['background']
    character.skills = request.json['skills']
    character.user_token = current_user_token.token

    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)

@api.route('/stats/<id>', methods = ['POST','PUT'])
@token_required
def update_stats(current_user_token, id):
    stats = Stats.query.get(id)

    stats.str = request.json['str']
    stats.dex = request.json['dex']
    stats.con = request.json['con']
    stats.int = request.json['int']
    stats.wis = request.json['wis']
    stats.cha = request.json['cha']
    stats.user_token = current_user_token.token

    db.session.commit()
    response = stats_schema.dump(stats)
    return jsonify(response)


@api.route('/classes/<id>', methods = ['POST','PUT'])
@token_required
def update_classes(current_user_token, id):
    classes = Classes.query.get(id)

    classes.art = request.json['art']
    classes.barb = request.json['barb']
    classes.bard = request.json['bard']
    classes.cle = request.json['cle']
    classes.dru = request.json['dru']
    classes.fig = request.json['fig']
    classes.mon = request.json['mon']
    classes.pal = request.json['pal']
    classes.ran = request.json['ran']
    classes.rog = request.json['rog']
    classes.sor = request.json['sor']
    classes.war = request.json['war']
    classes.wiz = request.json['wiz']
    classes.user_token = current_user_token.token

    db.session.commit()
    response = classes_schema.dump(classes)
    return jsonify(response)

@api.route('/subclasses/<id>', methods = ['POST','PUT'])
@token_required
def update_subclasses(current_user_token, id):
    subclasses = Subclasses.query.get(id)

    subclasses.art = request.json['art']
    subclasses.barb = request.json['barb']
    subclasses.bard = request.json['bard']
    subclasses.cle = request.json['cle']
    subclasses.dru = request.json['dru']
    subclasses.fig = request.json['fig']
    subclasses.mon = request.json['mon']
    subclasses.pal = request.json['pal']
    subclasses.ran = request.json['ran']
    subclasses.rog = request.json['rog']
    subclasses.sor = request.json['sor']
    subclasses.war = request.json['war']
    subclasses.wiz = request.json['wiz']
    subclasses.user_token = current_user_token.token

    db.session.commit()
    response = subclasses_schema.dump(subclasses)
    return jsonify(response)


@api.route('/skills/<id>', methods = ['POST','PUT'])
@token_required
def update_skills(current_user_token, id):
    skills = Skills.query.get(id)

    skills.arc = request.json['arc']
    skills.ani = request.json['ani']
    skills.ath = request.json['ath']
    skills.dec = request.json['dec']
    skills.his = request.json['his']
    skills.ins = request.json['ins']
    skills.inti = request.json['inti']
    skills.inv = request.json['inv']
    skills.med = request.json['med']
    skills.nat = request.json['nat']
    skills.perc = request.json['perc']
    skills.perf = request.json['perf']
    skills.pers = request.json['pers']
    skills.rel = request.json['rel']
    skills.soh = request.json['soh']
    skills.ste = request.json['ste']
    skills.sur = request.json['sur']
    skills.user_token = current_user_token.token

    db.session.commit()
    response = skills_schema.dump(skills)
    return jsonify(response)


# Delete
@api.route('/character/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)

@api.route('/stats/<id>', methods = ['DELETE'])
@token_required
def delete_stats(current_user_token, id):
    stats = Stats.query.get(id)
    db.session.delete(stats)
    db.session.commit()
    response = stats_schema.dump(stats)
    return jsonify(response)

@api.route('/classes/<id>', methods = ['DELETE'])
@token_required
def delete_classes(current_user_token, id):
    classes = Classes.query.get(id)
    db.session.delete(classes)
    db.session.commit()
    response = classes_schema.dump(classes)
    return jsonify(response)

@api.route('/subclasses/<id>', methods = ['DELETE'])
@token_required
def delete_subclasses(current_user_token, id):
    subclasses = Subclasses.query.get(id)
    db.session.delete(subclasses)
    db.session.commit()
    response = subclasses_schema.dump(subclasses)
    return jsonify(response)

@api.route('/skills/<id>', methods = ['DELETE'])
@token_required
def delete_skills(current_user_token, id):
    skills = Skills.query.get(id)
    db.session.delete(skills)
    db.session.commit()
    response = skills_schema.dump(skills)
    return jsonify(response)