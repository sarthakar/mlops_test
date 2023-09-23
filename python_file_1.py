total_samples = len(train_data) + len(test_data) + len(dev_data)
print(f'Total samples in the dataset: {total_samples}')

image_height, image_width = get_image_size(train_data[0]) 
print(f'Image size (height x width): {image_height} x {image_width}')
