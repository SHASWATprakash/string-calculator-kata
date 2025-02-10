from flask import Blueprint, request, jsonify
from services.calculator_service import StringCalculator

calculator_bp = Blueprint('calculator', __name__)
calculator = StringCalculator()

@calculator_bp.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        result = calculator.add(data.get("input", ""))
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
