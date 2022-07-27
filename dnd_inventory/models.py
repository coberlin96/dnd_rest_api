from cmath import atanh
import email
from platform import architecture
from click import password_option
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow
import secrets

from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
ma = Marshmallow()

db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    email = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    character = db.relationship('Character', backref = 'owner, lazy = True')


    def __init__(self, email, password = '', token = '', g_auth_verify = False):
        self.email = email,
        self.password = password
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self,length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def __repr__(self):
        return f"User {self.email} has been added"

class Character(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    stats = db.Column(db.String, db.ForeignKey('stats.id'), nullable=False)
    classes = db.Column(db.String, db.ForeignKey('classes.id'), nullable=False)
    subclasses = db.Column(db.String, db.ForeignKey('subclasses.id'), nullable=False)
    race = db.Column(db.String(150))
    subrace = db.Column(db.String(150), nullable = True)
    background = db.Column(db.String(150))
    skills = db.Column(db.String, db.ForeignKey('skills.id'), nullable=False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, stats, classes, subclasses, race, subrace, background, skills, user_token):
        self.id = self.set_id()
        self.name = name
        self.stats = stats
        self.classes = classes
        self.subclasses = subclasses
        self.race = race
        self.subrace = subrace
        self.background = background
        self.skills = skills
        self.user_token = user_token

    def __repr__(self):
        return f"{self.name} has been created and added to the database!"

    def set_id(self):
        return(secrets.token_urlsafe())


class Stats(db.Model):
    id = db.Column(db.String, primary_key=True)
    str = db.Column(db.Numeric(precision=2, scale=0))
    dex = db.Column(db.Numeric(precision=2, scale=0))
    con = db.Column(db.Numeric(precision=2, scale=0))
    int = db.Column(db.Numeric(precision=2, scale=0))
    wis = db.Column(db.Numeric(precision=2, scale=0))
    cha = db.Column(db.Numeric(precision=2, scale=0))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, str, dex, con, int, wis, cha, user_token):
        self.id = self.set_id()
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.user_token = user_token

    def set_id(self):
        return(secrets.token_urlsafe())

class Classes(db.Model):
    id = db.Column(db.String, primary_key=True)
    art = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    barb = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    bard = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    cle = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    dru = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    fig = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    mon = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    pal = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    ran = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    rog= db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    sor = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    war = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    wiz = db.Column(db.Numeric(precision=2, scale=0), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, art, barb, bard, cle, dru, fig, mon, pal, ran, rog, sor, war, wiz, user_token):
        self.id = self.set_id()
        self.art = art
        self.barb = barb
        self.bard = bard
        self.cle = cle
        self.dru = dru
        self.fig = fig
        self.mon = mon
        self.pal = pal
        self.ran = ran
        self.rog = rog
        self.sor = sor
        self.war = war
        self.wiz = wiz
        self.user_token = user_token

    def set_id(self):
        return(secrets.token_urlsafe())

class Subclasses(db.Model):
    id = db.Column(db.String, primary_key=True)
    art = db.Column(db.String(50), nullable = True)
    barb = db.Column(db.String(50), nullable = True)
    bard = db.Column(db.String(50), nullable = True)
    cle = db.Column(db.String(50), nullable = True)
    dru = db.Column(db.String(50), nullable = True)
    fig = db.Column(db.String(50), nullable = True)
    mon = db.Column(db.String(50), nullable = True)
    pal = db.Column(db.String(50), nullable = True)
    ran = db.Column(db.String(50), nullable = True)
    rog= db.Column(db.String(50), nullable = True)
    sor = db.Column(db.String(50), nullable = True)
    war = db.Column(db.String(50), nullable = True)
    wiz = db.Column(db.String(50), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, art, barb, bard, cle, dru, fig, mon, pal, ran, rog, sor, war, wiz, user_token):
        self.id = self.set_id()
        self.art = art
        self.barb = barb
        self.bard = bard
        self.cle = cle
        self.dru = dru
        self.fig = fig
        self.mon = mon
        self.pal = pal
        self.ran = ran
        self.rog = rog
        self.sor = sor
        self.war = war
        self.wiz = wiz
        self.user_token = user_token

    def set_id(self):
        return(secrets.token_urlsafe())


class Skills(db.Model):
    id = db.Column(db.String, primary_key=True)
    acr = db.Column(db.Boolean, nullable = True)
    ani = db.Column(db.Boolean, nullable = True)
    arc = db.Column(db.Boolean, nullable = True)
    ath = db.Column(db.Boolean, nullable = True)
    dec = db.Column(db.Boolean, nullable = True)
    his = db.Column(db.Boolean, nullable = True)
    ins = db.Column(db.Boolean, nullable = True)
    inti = db.Column(db.Boolean, nullable = True)
    inv = db.Column(db.Boolean, nullable = True)
    med = db.Column(db.Boolean, nullable = True)
    nat = db.Column(db.Boolean, nullable = True)
    perc = db.Column(db.Boolean, nullable = True)
    perf = db.Column(db.Boolean, nullable = True)
    pers = db.Column(db.Boolean, nullable = True)
    rel = db.Column(db.Boolean, nullable = True)
    soh = db.Column(db.Boolean, nullable = True)
    ste = db.Column(db.Boolean, nullable = True)
    sur = db.Column(db.Boolean, nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, user_token, ani, arc, ath, dec, his, ins, inti, inv, med, nat, perc, perf, pers, rel, soh, ste, sur):
        self.id = self.set_id()
        self.arc = arc
        self.ani = ani
        self.ath = ath
        self.dec = dec
        self.his = his
        self.ins = ins
        self.inti = inti
        self.inv = inv
        self.med = med
        self.nat = nat
        self.perc = perc
        self.perf = perf
        self.pers = pers
        self.rel = rel
        self.soh = soh
        self.ste = ste
        self.sur = sur
        self.user_token = user_token

    def set_id(self):
        return(secrets.token_urlsafe())


class CharacterSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'stats', 'classes', 'subclasses', 'race', 'subrace', 'background', 'skills']
class StatsSchema(ma.Schema):
    class Meta:
        fields = ['id', 'str', 'dex', 'con', 'int', 'wis', 'cha']
class ClassesSchema(ma.Schema):
    class Meta:
        fields = ['id', 'art', 'barb', 'bard', 'cle', 'dru', 'fig', 'mon', 'pal', 'ran', 'rog', 'sor', 'war', 'wiz']
class SubclassesSchema(ma.Schema):
    class Meta:
        fields = ['id', 'art', 'barb', 'bard', 'cle', 'dru', 'fig', 'mon', 'pal', 'ran', 'rog', 'sor', 'war', 'wiz']
class SkillsSchema(ma.Schema):
    class Meta:
        fields = ['id', 'arc', 'ani', 'ath', 'dec', 'his', 'ins', 'inti', 'inv', 'med', 'nat', 'perc', 'perf', 'pers', 'rel', 'soh', 'ste', 'sur']
class UserSchema(ma.Schema):
    class Meta:
        fields = ['email', 'password', 'g_auth_verify', 'token']



character_schema = CharacterSchema()
characters_schema = CharacterSchema(many = True)
stats_schema = StatsSchema()
multi_stats_schema = StatsSchema(many = True)
classes_schema = ClassesSchema()
multi_classes_schema = ClassesSchema(many = True)
subclasses_schema = ClassesSchema()
multi_subclasses_schema = ClassesSchema(many = True)
skills_schema = SkillsSchema()
multi_skills_schema = SkillsSchema(many = True)
user_schema = UserSchema()
