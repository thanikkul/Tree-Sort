# Description of this Program
# Author : Thanikkul Promsree
# Since : 2021-08-22
# Program Name : Tree Sort
# Program Language : Python
# Program Purpose : sorted list data

class TreeNode:  # สร้างคลาส TreeNode
    def __init__(self, data):
        self.data = data  # ค่า Data คือ ชุดข้อมูลที่เราต้องการ sort
        self.left = None  # กำหนด left คือ pointer เท่ากับ None
        self.right = None  # กำหนด right คือ pointer เท่ากับ None

    def Binary_insert(self, data):  # เป็น function เพื่อตรวจสอบข้อมูลที่เราเพิ่มเข้าไป
        if data < self.data:  # ถ้าต้องการเพิ่มข้อมูล ที่ น้อยกว่า ค่าปัจจุบัน
            if self.left:  # ตรวจสอบค่าทางด้านซ้าย
                self.left.Binary_insert(data)  # จะเรียก Method ที่มี data ซ้ำ
            else:  # กรณีอื่นจะแสดงว่า Node ด้านซ้ายของเราว่าง
                self.left = TreeNode(data)
        else:  # ถ้าค่ามากกว่าจะเพิ่มข้อมูลทางด้านขวา
            if self.right:  # ตรวจสอบค่าทางด้านขวา
                self.right.Binary_insert(data)  # จะเรียก Method ที่มี data ซ้ำ
            else:  # กรณีอื่นจะแสดงว่า Node ด้านขวาของเราว่าง
                self.right = TreeNode(data)

    def Format_infolder(self):  # เป็น function เพื่อคืนค่า data ตามลำดับ
        elements = []  # สร้าง list
        if self.left:  # ตรวจสอบค่าด้านซ้าย
            elements += self.left.Format_infolder()  # ส่งค่าคืนเพิ่มรายการเข้าไปใน list

        elements.append(self.data)
        if self.right:  # ตรวจสอบค่าด้านซ้าย
            elements += self.right.Format_infolder()  # ส่งค่าคืนเพิ่มรายการเข้าไปใน list

        return elements  # ส่งคืนค่าข้อมูล


def build_tree(elements):  # เป็น function เพื่อสร้างโครงสร้างข้อมูล แบบ tree
    print("PRE SORT:", elements)
    root = TreeNode(elements[0])  # กำหนด root เท่ากับ TreeNode Node แรก

    for i in range(1, len(elements)):  # ลูปข้อมูลตามจำนวนข้อมูลที่มีอยู่
        root.Binary_insert(elements[i])  # เพิ่มข้อมูลไปตรวจสอบ

    return root  # ส่งคืนค่า root


if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 4, 1, 1, 20, 9, 23, 18, 34])
    print("POST SORT:", numbers_tree.Format_infolder())
