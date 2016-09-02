from celery import shared_task
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import accuracy_score
from lib.util import timing_now, timing_elapsed_to_str
from lib.files import download_file
from service.compute.pipelines.util import create_task_dir, delete_task_dir
from service.compute.pipelines.stats.util import load_features, get_xy, save_model, upload_model_archive


# ----------------------------------------------------------------------------------------------------------------------
@shared_task(name='run_training_fold')
def run_training_fold(storage_id, train, test, index_column, target_column, exclude_columns, token):

    # # Create temporary folder for storing a local copy of the input file(s) as
    # # well as any intermediate files that are generated by the pipeline.
    # task_dir = create_task_dir()
    #
    # try:
    #     # Download and import the features
    #     file_path = download_file(storage_id, task_dir, token)
    #     features = load_features(file_path, index_col=index_column)
    #     X, y = get_xy(features, target_column=target_column, exclude_columns=exclude_columns)
    #
    #     # Start timing training procedure
    #     start = timing_now()
    #
    #     # Start training the classifier using a grid search approach for determining
    #     # the optimal hyper-parameters.
    #     param_grid = [{
    #         'C': [2 ** i for i in range(-5, 15, 2)],
    #         'gamma': [2 ** i for i in range(-15, 4, 2)]}]
    #     classifier = GridSearchCV(SVC(kernel='rbf'), param_grid=param_grid, scoring='accuracy')
    #     classifier.fit(X[train], y[train])
    #     y_pred = classifier.predict(X[test])
    #     y_true = y[test]
    #     accuracy = accuracy_score(y_true, y_pred)
    #
    #     # Record time elapsed, accuracy and optimal hyper parameters
    #     time_elapsed = timing_elapsed_to_str(start)
    #     print('Training fold time elapsed: {}'.format(time_elapsed))
    #     print('Classifier accuracy: {}'.format(accuracy))
    #     print('Best C: {}, best gamma: {}'.format(classifier.best_params_['C'], classifier.best_params_['gamma']))
    #
    # finally:
    #     # Clean up task directory under any circumstances, even error
    #     delete_task_dir(task_dir)
    #
    # return {
    #     'accuracy': accuracy,
    #     'C': classifier.best_params_['C'],
    #     'gamma': classifier.best_params_['gamma'],
    #     'time_elapsed': time_elapsed,
    # }

    print('Running task: run_training_fold')
    return {
        'accuracy': 0.72,
        'C': 0.01,
        'gamma': 0.00000056,
        'time_elapsed': '0 secs',
    }


# ----------------------------------------------------------------------------------------------------------------------
@shared_task(name='retrain_classifier')
def retrain_classifier(outputs, storage_id, repository_id, nr_folds, index_column, target_column,
                       exclude_columns, token):

    # # Extract accuracies, C and gamma values from the outputs
    # accuracies = []
    # Cs = []
    # gammas = []
    # for i in range(len(outputs)):
    #     accuracies.append(outputs[i]['accuracy'])
    #     Cs.append(outputs[i]['C'])
    #     gammas.append(outputs[i]['gamma'])
    #
    # # Average the accuracies
    # accuracy = sum(accuracies) / nr_folds
    # print('Average accuracy: {}'.format(accuracy))
    #
    # # Figure out which hyper-parameters to choose
    # max_accuracy = 0.0
    # max_C = 0.0
    # max_gamma = 0.0
    # for i in range(len(accuracies)):
    #     if accuracies[i] > max_accuracy:
    #         max_accuracy = accuracies[i]
    #         max_C = Cs[i]
    #         max_gamma = gammas[i]
    # print('Max. accuracy: {}, max. C: {}, max. gamma: {}'.format(max_accuracy, max_C, max_gamma))
    #
    # # Retrain classifier on all data using the optimal hyper-parameters
    # task_dir = create_task_dir()
    #
    # try:
    #     # Download the file and load its features
    #     file_path = download_file(storage_id, task_dir, token)
    #     features = load_features(file_path, index_col=index_column)
    #     X, y = get_xy(features, target_column=target_column, exclude_columns=exclude_columns)
    #
    #     # Train the classifier on all features with the optimal hyper-parameters
    #     classifier = SVC(kernel='rbf', C=max_C, gamma=max_gamma)
    #     classifier.fit(X, y)
    #
    #     # Save the classifier to disk and then upload it to storage service as regular file
    #     classifier_file_path = save_model(classifier, task_dir)
    #     classifier_id = upload_model_archive(classifier_file_path, repository_id, token)
    #
    # finally:
    #     # Delete temporary task directory even though errors may have occured
    #     delete_task_dir(task_dir)
    #
    # # Return average accuracy and the optimal hyper-parameters
    # return {
    #     'accuracy': accuracy,
    #     'C': max_C,
    #     'gamma': max_gamma,
    #     'classifier_id': classifier_id,
    # }

    print('Running task: retrain_classifier')
    return {
        'accuracy': 0.77,
        'C': 0.02,
        'gamma': 0.000065,
        'classifier_id': 'lkfjaslkfjsalkdjf',
    }