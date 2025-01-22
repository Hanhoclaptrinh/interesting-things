# Bộ câu hỏi 10 đề tài khác nhau
questions = (
    "1. Hiện tượng nào mô tả sự biến đổi của chất rắn thành chất lỏng khi nhiệt độ tăng?",
    "2. Năm 1975, chiến tranh Việt Nam kết thúc với sự kiện lịch sử nào?",
    "3. Hợp chất nào là sản phẩm chính khi axit sulfuric (H₂SO₄) phản ứng với natri hidroxit (NaOH)?",
    "4. Khi nói về DNA, cấu trúc của nó có dạng gì?",
    "5. Đại dương nào là lớn nhất thế giới?",
    "6. Ai là tác giả của tác phẩm 'Chí Phèo'?",
    "7. Đặc điểm nào dưới đây đúng với một cơ cấu truyền động đơn giản nhất?",
    "8. Giải phương trình bậc hai ax^2 + bx + c = 0, nghiệm của phương trình là gì?",
    "9. Công thức nào dùng để tính tốc độ ánh sáng trong chân không?",
    "10. Để chèn một hình ảnh vào trong tài liệu Microsoft Word, người dùng cần chọn công cụ nào?"
)

# Lựa chọn đáp án
options = (
    ("A. Nóng chảy", "B. Bay hơi", "C. Hóa rắn", "D. Sự ngưng tụ"),
    ("A. Ký kết Hiệp định Paris", "B. Giải phóng miền Nam", "C. Thành lập Cộng hòa xã hội chủ nghĩa Việt Nam", "D. Quân đội Mỹ rút khỏi Việt Nam"),
    ("A. NaOH", "B. Na2SO4", "C. Na2CO3", "D. H2O"),
    ("A. Mạch đơn", "B. Mạch kép xoắn", "C. Cầu", "D. Đoạn thẳng"),
    ("A. Đại Tây Dương", "B. Thái Bình Dương", "C. Ấn Độ Dương", "D. Bắc Băng Dương"),
    ("A. Nguyễn Du", "B. Nam Cao", "C. Tô Hoài", "D. Thạch Lam"),
    ("A. Gồm một động cơ điện và bánh răng", "B. Gồm một cơ cấu bánh răng và dây curoa", "C. Gồm một động cơ và một trục quay", "D. Gồm một bánh đà và một bộ truyền tín hiệu"),
    ("A. x = (-b ± √(b² - 4ac)) / 2a", "B. x = (-b ± √(b² + 4ac)) / 2a", "C. x = -b + c/a", "D. x = -b/a"),
    ("A. c = λ · f", "B. c = 1/λ", "C. c = f/λ", "D. c = √(1/με)"),
    ("A. Insert -> Text Box", "B. Insert -> Picture", "C. View -> Zoom", "D. Design -> Themes")
)

# Bộ đáp án
answers = (
    "A",  # Đáp án câu 1
    "B",  # Đáp án câu 2
    "B",  # Đáp án câu 3
    "B",  # Đáp án câu 4
    "B",  # Đáp án câu 5
    "B",  # Đáp án câu 6
    "C",  # Đáp án câu 7
    "A",  # Đáp án câu 8
    "A",  # Đáp án câu 9
    "B"   # Đáp án câu 10
)

guess = [] # Lưu đáp án user
score = 0 # Điểm
questions_num = 0 # Thứ tự câu hỏi

for question in questions:
    print("--------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    user_input = input("Nhập đáp án của bạn (A B C or D): ").upper().strip()
    guess.append(user_input) # Add câu trả lời vào mảng
    if user_input == answers[questions_num]:
        score += 10
        print("Correct!")
    else:
        print(f"Oops! Đáp án cho câu hỏi '{question}' là {answers[questions_num]}")
        score -= 10
    questions_num += 1

print("--------------------")

print(f"Điểm: {score} / 100")\

print("--------------------")
print("\t\tKết quả")
print("--------------------")
print("Đáp án: ", end=" ")
for ans in answers:
    print(ans, end=" ")

print()

print("Trả lời: ", end=" ")
for guess_ans in guess:
    print(guess_ans, end=" ")