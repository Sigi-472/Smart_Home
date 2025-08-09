from flask import Blueprint, request, jsonify
from datetime import datetime
from db_defs import get_engine, get_session, Notiz

note_api = Blueprint('note_api', __name__)  # Blueprint für deine API-Routen

@note_api.route("/note_api/save_note", methods=["POST"])
def api_save_note():
  data = request.get_json()

  notiz_text = data.get("notiz")
  priority = data.get("priorityint")
  datum_str = data.get("date")

  try:
    datum_obj = datetime.strptime(datum_str, "%Y-%m-%d").date()
  except Exception:
    return jsonify({"error": "Ungültiges Datum"}), 400

  session = get_session(get_engine())
  neue_notiz = Notiz(Notiz=notiz_text, Priority=priority, Datum=datum_obj)

  session.add(neue_notiz)
  session.commit()
  session.close()

  return jsonify({'message': 'Notiz gespeichert'})