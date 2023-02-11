from model import net
import torch
import pickle


def get_prediction(nitrogen, phosphorous, potassium, ph, temperature, humidity, rainfall):
    model = net(7, 22)
    model.load_state_dict(torch.load('model.hdf5'))
    x = torch.tensor([nitrogen, phosphorous, potassium,
                     temperature, humidity, ph, rainfall])
    prediction = model(x)

    with open("utils/encoder.pkl", "rb") as file:
        encoder = pickle.load(file)

    encoded_labels = encoder.inverse_transform(prediction)
    # DEBUG
    print("Encoded labels:", encoded_labels)

    return 'prediction'
