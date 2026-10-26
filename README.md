Welcome to the Computer Vision Project Tutorial! In this session, we'll talk about your computer vision projects. We will cover the creation of image datasets using annotation tools, a practical demonstration of one such tool, an overview of the YOLO (You Only Look Once) framework, and guidance on formatting and saving your dataset in YOLO's preferred format.

# Assignment: Computer Vision Project
This assignment aims to apply the skills and knowledge you have acquired about image datasets, the YOLO object detection framework, and image annotation tools. You are required to either create a new image dataset or annotate an existing dataset, focusing on one of the following computer vision tasks: classification, detection, segmentation, or tracking.  

 
 ## Tasks: 
 1. **Identify a Problem (this should be the same as the [discussion](https://canvas.sfu.ca/courses/13506/discussion_topics/237097?module_item_id=705914), unless you spoke with us and we approved a different version):**
    - Choose a problem or topic in computer vision that interests you.
    - The problem should align with one of the following tasks:
       - Classification, Detection, Segmentation, Pose estimation, Tracking 

2. **Dataset Creation/Enhancement:** Gather available datasets online <ins>AND</ins> add 30 new images/labels <ins>per person</ins>. Normally, the existing dataset will be used as training and your own data will be test data; if there are issues with dataset size you can also 2/3 of this data should be used as training data, the rest is for evaluation - but this needs to be justified in the report and approved by us. The structure of the dataset and annotations should be correctly added in the sub-folder structure for YOLO. This new data, if it does not have any privacy concerns, should be added to github. If privacy & security cannot be guaranteed, share a link to a zip folder with the correct sub-folder structure. If you're using another dataset in addition to yours, make sure you have sharing rights. If you do not have sharing rights, do not share it in neither github or as .zip, but rather share the link of the dataset you found it from.
    - **Step 1 - Find Existing Data:**
       - Collect and assemble a dataset of images relevant to your chosen problem.
       - Ensure the dataset is diverse and representative of the problem.
    - **Step 2 - Create New Data:**
       - Create new images/videos, 30 images per person, annotate the data using given annotation tools
    - **BONUS STEP:**
       - Perform data augmentation to increase your dataset size! You should've received feedback from us about whether this is required or not.
         
3. **Fine-Tuning YOLO with Your Custom Dataset**
    - Clone the YOLO repository from its official GitHub page or the version specified in the course materials.
    - Integrate your custom dataset into the YOLO framework (transfer learning).
    - Fine-tune the YOLO model using your dataset with one specific set of hyperparameters. This will be called as your **baseline model**.
    - Save your fine-tuned model, and evaluate the accuracy.
    - This step will be done as a group in collaboration.
5. **Hyperparameter tuning:**
    - <ins>Each person</ins> in the group picks one hyperparameters to change in 3 different values than the original value it had from Step 3. Compares their own results to the model performance at Step 3.
    - The group altogether evaluates all results, and reports the best hyperparameter or a combination thereof as the final best performing model. Writes down justification of their selection and brief discussion on why that model might've performed the best.
    - Members of the same group should not pick the same hyperparameter or value.
      
7. **Report:** Provide a document outlining:
    - Your **chosen problem** and its significance.
    - **Dataset report:**
       - Explain how you created your data, this includes links to the online resources and the steps to create the dataset as detailed above. Add links for annotation tools or any existing images.
       - The methodology used for collecting and annotating the dataset.
       - Example snippets from your dataset (showing both images and labels)
       - Bias and privacy issues you see with the datasets you used.
    - **Model analysis:**
       - A detailed evaluation of your baseline model’s performance.
       - Evaluation of each member's fine-tuned model based on different hyperparameter combinations.
       - Discussion of the best performing model.
       - A critical analysis of the model's shortcomings and ethical considerations. 
    - **Challenges** faced during any of above steps and how they were addressed.

### Submission Format: 
Submit your report as a PDF file on canvas, the PDF should include the links to code & datasets in github. Make sure your links work properly.  

# Annotation Guidelines: 
- Clearly define the labels or annotations you will use. 
- For detection, segmentation, or tracking tasks, annotate each image with bounding boxes or segmentation masks, as appropriate.
- Ensure annotations are accurate and consistent.

## Annotation tools: 

You can use one of the following tools for annotation: 

1. Label Studio 

    **Description:** Label Studio is an open source data labeling tool that supports multiple projects, users, and data types in one platform. It allows you to perform different types of labeling with many data formats. Also, you can integrate Label Studio with machine learning models to supply predictions for labels (pre-labels). 

    **Website:** [Label Studio](https://labelstud.io/)

    **Tutorials:** 
      *Text:* [Label Studio Documentation — Overview of Label Studio](https://labelstud.io/guide/get_started.html#Quick-start)
   
      *Video:* [Quickly Create Datasets for Training YOLO Object Detection with Label Studio | Label Studio](https://labelstud.io/blog/quickly-create-datasets-for-training-yolo-object-detection-with-label-studio/) 

 

3. Makesense.ai 

    **Description:** Makesense.ai is a free, user-friendly online tool for labeling photos, ideal for quick annotation tasks. 

   **Website:** [Makesense.ai](https://www.makesense.ai/) 

    GitHub: [SkalskiP/make-sense: Free to use online tool for labelling photos. https://makesense.ai github.com](https://github.com/SkalskiP/make-sense)

    **Tutorials:** 

      *Text:* [Annotate Your Image — Using Online Annotation Tool! | by Sabina Pokhrel | Towards Data Science](https://medium.com/data-science/annotate-your-image-using-online-annotation-tool-52d0a742daff) 

     *Video:* https://youtu.be/7nYYb6vwCjM 

 

4. VGG Image Annotator (VIA) 

    **Description:** VGG Image Annotator is a simple and standalone manual annotation software for image, audio and video. VIA runs in a web browser and does not require any installation or setup. 

    **Website:** [Visual Geometry Group - University of Oxford](https://www.robots.ox.ac.uk/~vgg/software/via/) 

    **Tutorials:** 

      *Text:*   [Visual Geometry Group - University of Oxford](https://www.robots.ox.ac.uk/~vgg/software/via/) 

      *Video:* https://www.youtube.com/watch?v=-3WVSxNLk_k 

 

5. Roboflow 

     **Description:**  Roboflow primarily serves as an annotation tool for computer vision models. It streamlines the annotation process, allowing users to label and annotate images efficiently for tasks like object detection. Additionally, it integrates with popular frameworks for model training and deployment. 

      For individuals with personal projects, school assignments, or research projects, Roboflow offers the Public plan to encourage exploration of computer vision. All projects on the Public plan are shared on Roboflow Universe. They offer to work upto 10000 source images for annotation.  

      What i liked about Roboflow was that you can directly upload a video file and it will create images from it itself.  

     **Website:** [Roboflow](https://roboflow.com) => Select public plan for free! 

    **Tutorials:**  
      *Text:*  [Introduction - Roboflow Docs](https://docs.roboflow.com/)
   
      *Video:* [Getting Started with Roboflow](https://www.youtube.com/watch?v=O-ZPxTpb2Yg) 

 



 

 

 
