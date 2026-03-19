# Rayoscan AI Diagnostics - Tooth Number Detection using YOLO11
This project was developed as part of the AI Intern selection assignment for Rayoscan AI Diagnostics.

The objective was to train a YOLO-based object detection model on annotated dental images for tooth numbering detection. The final pipeline includes dataset validation, preprocessing, model training, validation, and inference.

## Approach
- Verified dataset structure and annotation consistency
- Split dataset into train/validation/test sets
- Detected and removed 3 corrupted annotation files containing mixed bounding-box and polygon-format labels
- Trained a YOLO11n model on the cleaned dataset
- Evaluated performance using Precision, Recall, mAP50, and mAP50-95
- Generated sample prediction outputs on test images

## Repository Structure
- `src/train.py` - model training
- `src/predict.py` - inference on test images
- `src/validate.py` - evaluation
- `src/dataset_check.py` - dataset validation and cleaning
- `weights/best.pt` - trained model weights
- `sample_outputs/` - sample prediction results
- `reports/` - PDF report

## Installation

```bash
git clone <your-repo-link>
cd rayoscan-tooth-detection
pip install -r requirements.txt

## 6. Training command
```markdown
## Training

```bash
python src/train.py


## 7. Validation command
```markdown
## Validation

```bash
python src/validate.py


## 8. Inference command
```markdown
## Inference

```bash
python src/predict.py


## 9. Dataset note
```markdown
## Dataset
The dataset used for this assignment consists of annotated dental images for tooth numbering detection.

Note: The original dataset is not included in this repository due to assignment/data-sharing constraints.

## Results

Final YOLO11n baseline performance after 30 epochs:

- Precision: 0.417
- Recall: 0.772
- mAP@50: 0.514
- mAP@50-95: 0.354

## Observations
- Tooth numbering is a challenging multiclass detection task due to visual similarity among adjacent teeth
- Some classes performed better than others, indicating class-wise variation in detection difficulty
- During preprocessing, 3 corrupted annotation files were identified and removed to ensure YOLO-compatible training

## Future Improvements
- Train larger YOLO variants such as YOLO11s on GPU
- Perform hyperparameter tuning
- Improve class naming using actual tooth-number labels
- Expand data cleaning and augmentation

## Sample Predictions
Example outputs are available in the `sample_outputs/` folder.
