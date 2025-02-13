import time

from antminermonitor.blueprints.asicminer.models import Miner
from flask import Blueprint, jsonify
from flask_login import login_required
from lib.pycgminer import (get_total,
                           get_summary,
                           get_pools,
                           get_stats,
                           )

antminer_json = Blueprint('antminer_json',
                          __name__,
                          template_folder='../templates',
                          )


@antminer_json.route('/<ip>/summary')
@login_required
def summary(ip):
    output = get_summary(ip)
    return jsonify(output)


@antminer_json.route('/<ip>/pools')
@login_required
def pools(ip):
    output = get_pools(ip)
    return jsonify(output)


@antminer_json.route('/<ip>/stats')
@login_required
def stats(ip):
    output = get_stats(ip)
    return jsonify(output)


@antminer_json.route('/all/total')
@login_required
def total():
    res = dict({'timestamp': int(time.time())})
    total = []
    miners = Miner.query.all()
    for miner in miners:
        info = dict({"IP": miner.ip})
        info.update(get_total(miner.ip))
        total.append(info)
    res.update({'total': total})
    return res
