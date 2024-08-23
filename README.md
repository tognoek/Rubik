# WELCOME TOGNOEK
* Sản phẩm mô phỏng Rubik 3x3
* Các công thức được tìm trên wiki và sử dụng GPT 4 để tìm hiểu
* [Basic 3D rotations](https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions)
* Cùng với cách xoay trên rubik trên wiki
* [Các cách giải chính](https://vi.wikipedia.org/wiki/L%E1%BA%ADp_ph%C6%B0%C6%A1ng_Rubik#C%C3%A1c_c%C3%A1ch_gi%E1%BA%A3i_ch%C3%ADnh)
* Vẽ 3D lên mặt phẳng 2D dựa trên tọa độ x, y
* Các phím bấm
  - Sử dùng x, y, z để xoay toàn bộ rubik theo các trục tương ứng
  - Có 6 cách xoay cơ bản là B, D, F, L, R, U tương ứng với các phím trên bàn phím
  - Phím s để xuất data của rubik, mình xuất ra cube và phần angle của từng block
  - Phím p để đưa rubik về độ lệch x: 6, y : 6, z : 6
* Mô tả code
  - Một class để thực hiện xoay ma trận 
  - Một class Block gồm các phương thức để cập nhật và vẽ Block
  - Class Rubik đảm nhiệm việc xoay rubik
  - File main.py là file chạy chương trình
* Cài đặt 2 thư viện là numpy và pygame theo phiên bản ở requirements.txt 