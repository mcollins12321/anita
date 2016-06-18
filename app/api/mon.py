from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from app.models import Mon


@api.route('/<ip_db>/mon/nbufs')
def get_mon_nbufs(ip_db):
    # print session['ip']
    # print session['db']
    # print session['ip_db']
    mons =getattr(Mon,ip_db).limit(1000).all()
    return jsonify({'mon_nbufs': [item.nbuf for item in mons], 'mon_nows': [item.now for item in mons]})
    # return jsonify({'hk': [item.now&mask for item in hks]})

@api.route('/<ip_db>/mon/<nbuf>')
def get_mon(ip_db, nbuf):

	## This will print a value into the command prompt with the first nbuf value that works
	# print "---------------- getattr >"
	# print getattr(Mon,ip_db).first().nbuf
	# print "---------------- getattr <"

	mon =getattr(Mon,ip_db).filter_by(nbuf=nbuf).first()
	return jsonify({'mon': mon.to_json()})
