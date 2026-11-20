#  dataset split
# You have 1000 samples and want an 80/20 train/test split

total_samples = 1000
train_ratio = 0.8
train_size = total_samples * train_ratio # 800.0
test_size = total_samples - train_size # 200.0
print("Train:", train_size, "Test:", test_size)




# Note that the results are floats (800.0). In Lecture 4 you will learn int() to convert them to whole
# numbers, which ML libraries need.