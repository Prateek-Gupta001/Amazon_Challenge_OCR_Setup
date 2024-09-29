import matplotlib.pyplot as plt
import requests
from io import BytesIO
import torch
import numpy as np
import pandas as pd
import os
import multiprocessing
from functools import partial
from tqdm import tqdm
from pathlib import Path
import time
from PIL import Image
import urllib.request
import cv2
import re
from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
import requests
from io import BytesIO
