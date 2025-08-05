{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a94edecd-7c5a-4e89-a66e-4fde164b9d74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PC\\miniconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3558: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "with open(\"gbr_model.pkl\", \"rb\") as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    data = request.get_json()\n",
    "    features = data.get(\"features\")\n",
    "    if features is None:\n",
    "        return jsonify({\"error\": \"No features provided\"}), 400\n",
    "    features_np = np.array(features).reshape(1, -1)\n",
    "    prediction = model.predict(features_np)[0]\n",
    "    return jsonify({\"prediction\": prediction})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27b63979-80b1-41c0-aee5-e08b97a67f9d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
