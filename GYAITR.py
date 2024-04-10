try:
    import cv2, os, time
except ModuleNotFoundError:
    os.system("pip install opencv-python")
    os.system("pip install os")
    os.system("pip install time")
    
    os.system("clear")

Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
Gray = "\033[1;39m"
DarkRed = "\033[2;31m"
DarkBlue = "\033[2;34m"
DarkPink = "\033[2;35m"
DarkCyan = "\033[2;36m"

print("""
                                      :~~~~?J5PB#&&&##BP5J7^.
                                  ^J5PB&&&&&&&&@@@@@@@@@@@@@#GPYJ7^
                              .~?G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G7
                           :?G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7.
                         .~5&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&7
                        :?PB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y 
                       ^?P#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@! 
                      :JB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@P7.
                     :P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&B@@#B@@@&PJ5PBGG@@@B
                     J@@@@@@@@@@@@@@@@@@@BPB#&&&&@@@@@@@PYBYJPP5JJY555?Y#@#:
                    ~P@@@@@@@@@@@@@@@@@@@#?7??^::!?YG#&BY??JG#BGB&@@@@&GGB~
                   .?B@@&@@@@@@@@@@@@@@@@@&B55!.    J5YJJG&@&@@&@@@@@@@@@@#P?^
                   :J&@B@@@@@@@@@@@@@@@@@@@@@#B577JB@@BB@@@GP@@@@@@@@@@@@@@@@@B?:
                   :P&P@&B@@@@@@@@@@@@@@@@@@@@&&&&@@@@@#&@@B@@@@@@@@@@@@@@@@@@@@&5^
                   7PJB@P&@@@@@@@@@@@@@@@@@@@@@@@@@@@#G?JP#&@@@@@@@@@@@@@@@@@@@@@@@Y
                  ~?7G@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@#555YPBPB&@@@@@@@@@@@@@@@@@@@@@@G.
                 .!^5@@@@@@&@@@@@@@@@#@@@@@@@BB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P
                   ?&@@@@@G&@@@@@@@@@&@@@@@@#GGBB####&&##&@@@@@@@@@@@@@@@@@@@@@@@@@@@&:
                  ~P#&@@@@B@@@@@@@@@@@@@@@@##GGGGGB##&&&&#BBB###&&&&&&&&&&&&&@@@@@@@@@~
                 :?JP@@@@@@@@@@@@@@@@@@@@@@@#BP555PPPP55GB#&&&&#BBG5J????JJ7^^^~!?5#@@~
                :??J&@@@@@@@@#&@&@@@@@@@@@@@@@@&#B5YJJ??????JYJJJ????????!.        .PB^
               :!!7G@@@@@@@@@@@@&&@@@@#&@@@&#BG5YJ???????????????????????7.         :!
                 ~J&@@@#&@&@@@@@@@&BPY??YPB##BG55?????????????????????????!          
                .??Y&@55PB&@@@@@@@&&BGB#BGGGGPP5J??????????????????????????.
                ~J?P@P75#@@@@@@@@@@@@@@@@@@&#G5Y??????J???????????????????J~
                7??BG?G@@@@@@@@@@@@@&#BP5YJ?777?J5PGB##PGBJ?????????????????~
               .????J#@@@@@@@&BGP5YJ???????J5GB&@@@@@@@@BJ???????????????????~
               :???5@@@###GYJJJJJY5PBBPY5G#@@@@@@@@@@&GJ7?????????????????????7:
               :?Y#@@@&BBGPGB###&@@&G5G&@@@@@@@@@@&B5?7?Y???????????????????????~.
               ?#@@&#B##&@@@@@@@@@#B#@@@@@@@@&#BGY??J5B&G?????????????????????????^
            :75P55Y5B&@@@@@@@@@#GG&@@@&BBGPYJ???7J#&@@&57?5????????????????????????~
            ^~..~5#@&@@@@@@#BPY5#@@#PJ??????????5@@@#5??5&G?????Y???????????????????!
              :7G#BB#&#BGPPGB#&&BPYJ5PPY7??J??P&@#PJ??Y#@GJJ??YB#?????????????????7^?^
             ~??J555JJYPB&@@&#GGGB#BGP5PGB#5Y#&GJ??5B&@@#BGJ7G@@5??????????????????^.!
            !J????7?5B#&@@@@##&#BBB#&@@@@#5JG5??5B@@@@&#BBJ?G@@P????????????????????.
           ~J??!!7JG#&@@@@@@@&&@@@@@@@&G555P5JG&@@&#PP#&@BY&@#Y7?J?????????????????J~
          :7!^.^75B@@@@@@@@@@@@@@@&BGPPB&&BB#@@@@@&5Y&@@BY&@B?7JB#???????????~???7:!7
          .   !5#@@@@@@&#BGP5555PPPG#&&#B#&@@@@@@GJP@@@BY&@G??P@@Y??????????! .!??  ^
            :J#&#BP5J7~:..:~YB&&#BBBPPG#@@@@@@#P?JB@@@PJ&@57JB@@5???????????^   :7.
           ~?Y?^:.   .:~7YPGGPJ~. :JB&@@@@&BP?~!G@@@&YJ&#J7Y&@&Y?????????77?.    .
          ^~:       :~~~~^.    ^?G&@@@@#PY~: .?#@@@P!~#P?7?@@GJ7^~??????7 ~7
                           :!YPBG5Y?~!^.    !#@@&P!. ?~.::##Y?~. .??????! ^^
                          .^~:.           .5@@#Y^   .    YB?~.    ^????J~ .
                                         :G#Y~.         ~5~.       !????.
                                         ^~             !:          7?J~
           .^!!777!~^.                                 ..           :?7
        .!JJ7~:...:~7J?:  ::..                                       :.
      :?Y!.  :~!!!~   ^G  G777Y!     ::.                                   ..  ^!!777!777^
     75~   !J?~:.:!P!!7J  B.  J5   .YJ7775~    7777!!.     .7777^ 77777777777Y G~:..::. :?J
   .5J   ^5?.      :!^.   G:  75  75~  ^Y?.   5?..::57     JJ::JJ Y....  .::~P 5^ .P7!?7  J7
  .G?   7P: .YJ?7!~:      P~  !Y:5?  :JJ:    5?  ^  J?     5~  Y! Y775^  5?~~^ J7  P.  P: ^P
  5Y   !G. :G7 .:~!7P?    57  !#Y^ .?5~     5?  5P  ?J     P.  P^    Y~  P^    ~Y  Y?^?J  J?
 ^B.  .B^  :J75!   !P:    ?Y  ^!  !5!      57  JG5  7Y    :P  .G.    Y~  5^    :P  ^!~: :Y?
 !G   ^#.    ?P:  7P.     !P    ~5?.     .P7  JJ~5  75    !5  ^G     5~  5^     P:  7?^ :P~
 :B^   JY!~^JP.  ?P.      JJ   YY:      .P7  JY ~P  ~P    J?  !5     P~  5^     Y~ .G^Y~ .Y7
  ~P!.  .~!!!   J5       !G   ?5       .P7  ^G?7YY  ~P    5!  J?     P~  5:     7J  5^ Y!  J?
   .?J?!~::.:^~YY       :B^  ~G.      .P7  .:.::.   ~G    G:  P!     P~  P:     ^5  ??  J7  JY
      :^~!777!!^        G7  .G~      .P!  ~P7777Y7  :G   :G   G:     P^  P:     .G. 7P   ??777
                       :5??75?      :G!  ~G:    ?Y  :G   ~P  :G      P~.:G:      ??77~
                         ..::       !P??JP^     !G?7?B.  !P7?YY      7J77!""")

time.sleep(3)
after_sleep1 = "\n\033[1;37mWelcome To GYAITR The AI System For Handling Images & Videos \U0001f44b\U0001f3fd."
print(after_sleep1)

time.sleep(3)
after_sleep2 = """\n\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mRead Images Dimensions & Pixels
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mOpen Images & Play Videos & Camera
\033[1;37m[\033[1;33m3\033[1;37m]\033[1;33m - \033[1;37mResize Images & Videos
\033[1;37m[\033[1;33m4\033[1;37m]\033[1;33m - \033[1;37mEdit Images & Videos"""
print(after_sleep2)

option = input("Choose \033[1;33m: \033[1;37m")

if option == "1" or option == "Read Images Dimensions & Pixels":
    img_name1 = input("Enter The Img Name Or Path \033[1;33m: \033[1;37m")
    img_read1 = cv2.imread(img_name1)
    print(img_read1)

    pixels = img_read1.size
    dim1 = img_read1.shape
    print(f"Number Of Pixels \033[1;33m:\033[1;37m {pixels} | Dimensions \033[1;33m:\033[1;37m {dim1}")

    try:
        pixels = img_read1.size
        dim1 = img_read1.shape
    except AttributeError: print("\033[1;31mPlease Check That The Img Name Or Path is Correct!")
    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")
    exit()

if option == "2" or option == "Open Images & Play Videos & Camera":
    choose_option2 = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37mImages
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37mVideos
\033[1;37m[\033[1;33m3\033[1;37m] \033[1;33m- \033[1;37mCamera \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")

    if choose_option2 == "1" or choose_option2 == "Images":
        img_name2 = input("Enter The Img Name Or Path \033[1;33m: \033[1;37m")
        img_read2 = cv2.imread(img_name2)
        img_open2 = cv2.imshow('Img Name', img_read2)

        try: img_open2 = cv2.imshow('Img Name', img_read2)
        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choose_option2 == "2" or choose_option2 == "Videos":
        vid_name1 = input("Enter The Vid Name Or Path \033[1;33m: \033[1;37m")
        vid_read1 = cv2.VideoCapture(vid_name1)

        while True:
            ret, frame = vid_read1.read()
            vid_open1 = cv2.imshow('Vid Name', frame)

            if cv2.waitKey(1) & 0xff == ord('q'): break
            
        try: vid_open1 = cv2.imshow('Vid Name', frame)
        except Exception as error_opening_vid:
            print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")
    elif choose_option2 == "3" or choose_option2 == "Camera":
        cam_read = cv2.VideoCapture(0)

        while True:
            ret, video = cam_read.read()
            cam_open = cv2.imshow('Cam', video)

            if cv2.waitKey(1) & 0xff == ord('q'): break
    else: print("\033[1;31mPlease Check The Correct Option!")

if option == "3" or option == "Resize Images & Videos":
    choose_option3 = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37mImages
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37mVideos
\033[1;37mChoose \033[1;33m: \033[1;37m""")

    if choose_option3 == "1" or choose_option3 == "Images":
        img_name3 = input("Enter The Img Name Or Path \033[1;33m: \033[1;37m")
        img_read3 = cv2.imread(img_name3)

        resizemode_img = input("""\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mDownScale (Decrease The Size Of The Img)
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mUpScale (Increase The Size Of The Img)
\033[1;37m[\033[1;33m3\033[1;37m]\033[1;33m - \033[1;37mResize Only The Width (Increase Or Decrease The Width Of The Img Keeping Height Unchanged)
\033[1;37m[\033[1;33m4\033[1;37m]\033[1;33m - \033[1;37mResize Only The Height (Increase Or Decrease The Height Of The Img Keeping Width Unchanged)
\033[1;37m[\033[1;33m5\033[1;37m]\033[1;33m - \033[1;37mResize To Specific Width And Height
\033[1;37mChoose \033[1;33m: \033[1;37m""")

        if resizemode_img == "1" or resizemode_img == "DownScale (Decrease The Size Of The Img)":
            print(f"Original Dimensions : {img_read3.shape}")

            img_scale = 60
            img_width = int(img_read3.shape[1] * img_scale / 100)
            img_height = int(img_read3.shape[0] * img_scale / 100)
            dim2 = (img_width, img_height)
            
            new_img_size1 = cv2.resize(img_read3, dim2, interpolation=cv2.INTER_AREA)

            print(f"Resized Dimensions : {new_img_size1.shape}")

            img_open3 = cv2.imshow('Img Name', new_img_size1)

            try: img_open3 = cv2.imshow('Img Name', new_img_size1)
            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            img_save1 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if img_save1 == "Y" or img_save1 == "y":
                choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.DS.png', new_img_size1)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.DS.png', new_img_size1)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.DS.jpg', new_img_size1)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.DS.jpg', new_img_size1)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            elif img_save1 == "N" or img_save1 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif resizemode_img == "2" or resizemode_img == "UpScale (Increase The Size Of The Img)":
            print(f"Original Dimensions : {img_read3.shape}")

            img_scale = 200
            img_width = int(img_read3.shape[1] * img_scale / 100)
            img_height = int(img_read3.shape[0] * img_scale / 100)
            dim3 = (img_width, img_height)

            new_img_size2 = cv2.resize(img_read3, dim3, interpolation=cv2.INTER_AREA)

            print(f"Resized Dimensions : {new_img_size2.shape}")

            img_open3 = cv2.imshow('Img Name', new_img_size2)

            try: img_open3 = cv2.imshow('Img Name', new_img_size2)
            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            img_save2 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if img_save2 == "Y" or img_save2 == "y":
                choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.US.png', new_img_size2)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.US.png', new_img_size2)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.US.jpg', new_img_size2)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.US.jpg', new_img_size2)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            elif img_save2 == "N" or img_save2 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif resizemode_img == "3" or resizemode_img == "Resize Only The Width (Increase Or Decrease The Width Of The Img Keeping Height Unchanged)":
            print(f"Original Dimensions : {img_read3.shape}")
            
            img_width = 440
            img_height = img_read3.shape[0]
            dim4 = (img_width, img_height)

            new_img_size3 = cv2.resize(img_read3, dim4, interpolation=cv2.INTER_AREA)

            print(f"Resized Dimensions : {new_img_size3.shape}")

            img_open3 = cv2.imshow('Img Name', new_img_size3)

            try: img_open3 = cv2.imshow('Img Name', new_img_size3)
            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            img_save3 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if img_save3 == "Y" or img_save3 == "y":
                choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.ROTW.png', new_img_size3)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.ROTW.png', new_img_size3)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)
                    cv2.imwrite('Img Name RS.ROTW.jpg', new_img_size3)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.ROTW.jpg', new_img_size3)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
            elif img_save3 == "N" or img_save3 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif resizemode_img == "4" or resizemode_img == "Resize Only The Height (Increase Or Decrease The Height Of The Img Keeping Width Unchanged)":
            print(f"Original Dimensions : {img_read3.shape}")
            
            img_width = img_read3.shape[1]
            img_height = 440
            dim5 = (img_width, img_height)

            new_img_size4 = cv2.resize(img_read3, dim5, interpolation=cv2.INTER_AREA)

            print(f"Resized Dimensions : {new_img_size4.shape}")

            img_open3 = cv2.imshow('Img Name', new_img_size4)
            
            try: img_open3 = cv2.imshow('Img Name', new_img_size4)
            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            img_save4 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if img_save4 == "Y" or img_save4 == "y":
                choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.ROTH.png', new_img_size4)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.ROTH.png', new_img_size4)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.ROTH.png', new_img_size4)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.ROTH.png', new_img_size4)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            elif img_save4 == "N" or img_save4 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif resizemode_img == "5" or resizemode_img == "Resize To Specific Width & Height":
            print(f"Original Dimensions : {img_read3.shape}")
            
            img_width = 350
            img_height = 450
            dim6 = (img_width, img_height)

            new_img_size5 = cv2.resize(img_read3, dim6, interpolation=cv2.INTER_AREA)

            print(f"Resized Dimensions : {new_img_size5.shape}")

            img_open3 = cv2.imshow('Img Name', new_img_size5)

            try: img_open3 = cv2.imshow('Img Name', new_img_size5)
            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            img_save5 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if img_save5 == "Y" or img_save5 == "y":
                choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.RTSWH.png', new_img_size5)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.RTSWH.png', new_img_size5)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                    directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                    os.chdir(directory_img)

                    cv2.imwrite('Img Name RS.RTSWH.jpg', new_img_size5)
                    print("Successfully Saved!")

                    try: cv2.imwrite('Img Name RS.RTSWH.jpg', new_img_size5)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            elif img_save5 == "N" or img_save5 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        else:
            print("\033[1;31mPlease Check The Correct Option!")
    elif choose_option3 == "2" or choose_option3 == "Videos":
        vid_name2 = input("Enter The Vid Name Or Path \033[1;33m: \033[1;37m")
        vid_read2 = cv2.VideoCapture(vid_name2)

        resizemode_vid = input("""\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mDownScale (Decrease The Size Of The Img)
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mUpScale (Increase The Size Of The Img)
\033[1;37mChoose \033[1;33m: \033[1;37m""")
        
        if resizemode_vid == "1" or resizemode_vid == "DownScale (Decrease The Size Of The Vid)":
            def rescale_frame1(frame, scale=0):
                vid_width = int(frame.shape[1] * scale)
                vid_height = int(frame.shape[0] * scale)
                dim7 = (vid_width, vid_height)

                return cv2.resize(frame, dim7, interpolation=cv2.INTER_AREA)
                new_vid_size1 = cv2.resize(frame, dim7, interpolation=cv2.INTER_AREA)
                
            while True:
                isTrue, frame = vid_read2.read()
                frame_resized = rescale_frame1(frame, scale=0.6)
                vid_open2 = cv2.imshow('Vid Name', frame_resized)
                
                if cv2.waitKey(1) & 0xff == ord('q'): break

            try: vid_open2 = cv2.imshow('Vid Name', frame_resized)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_read2.release()
            cv2.destroyAllWindows()

            vid_save1 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save1 == "Y" or vid_save1 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name RM.DS.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open2)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name RM.DS.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open2)
                except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save1 == "N" or vid_save1 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif resizemode_vid == "2" or resizemode_vid == "UpScale (Increase The Size Of The Vid)":
            def rescale_frame2(frame, scale=0):
                vid_width = int(frame.shape[1] * scale)
                vid_height = int(frame.shape[0] * scale)
                dim8 = (vid_width, vid_height)

                return cv2.resize(frame, dim8, interpolation=cv2.INTER_AREA)
                new_vid_size2 = cv2.resize(frame, dim8, interpolation=cv2.INTER_AREA)

            while True:
                isTrue, frame = vid_read2.read()
                frame_resized = rescale_frame2(frame, scale=0.2)
                vid_open2 = cv2.imshow('Vid Name', frame_resized)
                
                if cv2.waitKey(1) & 0xff == ord('q'): break

            try: vid_open2 = cv2.imshow('Vid Name', frame_resized)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            vid_save2 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save2 == "Y" or vid_save2 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name RS.US.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open2)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name RS.US.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open2)
                except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save1 == "N" or vid_save1 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
    else:
        print("\033[1;31mPlease Check The Correct Option!")
if option == "4" or option == "Edit Images & Videos":
    choose_option4 = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37mImages
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37mVideos
\033[1;37mChoose \033[1;33m: \033[1;37m""")
    if choose_option4 == "1" or choose_option4 == "Images":
        img_name4 = input("Enter The Img Name Or Path \033[1;33m: \033[1;37m")
        img_read4 = cv2.imread(img_name4)

        choose_edit = input("""\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mConvert Colors
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mAdd Effects
Choose \033[1;33m: \033[1;37m""")
        if choose_edit == "1" or choose_edit == "Convert Colors":
            choose_color = input("""\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mRGB → Gray
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mRGB → HSV
\033[1;37m[\033[1;33m3\033[1;37m]\033[1;33m - \033[1;37mRGB → LAB
\033[1;37m[\033[1;33m4\033[1;37m]\033[1;33m - \033[1;37mRGB → XYZ
\033[1;37m[\033[1;33m5\033[1;37m]\033[1;33m - \033[1;37mRGB → YCrCb
\033[1;37m[\033[1;33m6\033[1;37m]\033[1;33m - \033[1;37mLAB → RGB
\033[1;37m[\033[1;33m7\033[1;37m]\033[1;33m - \033[1;37mXYZ → RGB
\033[1;37m[\033[1;33m8\033[1;37m]\033[1;33m - \033[1;37mYCrCb → RGB
Choose \033[1;33m: \033[1;37m""")
            if choose_color == "1" or choose_color == "RGB → Gray":
                cvt_img_color1 = cv2.cvtColor(img_read4, cv2.COLOR_RGB2GRAY)
                img_open4 = cv2.imshow('Img Name', cvt_img_color1)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color1)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save6 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save6 == "Y" or img_save6 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC1.png', cvt_img_color1)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC1.png', cvt_img_color1)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC1.jpg', cvt_img_color1)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC1.jpg', cvt_img_color1)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save6 == "N" or img_save6 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else:
                    print("\033[1;31mPlease Check The Correct Option!")
                    exit()
            elif choose_color == "2" or choose_color == "RGB → HSV":
                cvt_img_color2 = cv2.cvtColor(img_read4, cv2.COLOR_RGB2HSV)
                img_open4 = cv2.imshow('Img Name', cvt_img_color2)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color2)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save7 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save7 == "Y" or img_save7 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC2.png', cvt_img_color2)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC2.png', cvt_img_color2)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC2.jpg', cvt_img_color2)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC2.jpg', cvt_img_color2)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save7 == "N" or img_save7 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!") exit()
            elif choose_color == "3" or choose_color == "RGB → LAB":
                cvt_img_color3 = cv2.cvtColor(img_read4, cv2.COLOR_RGB2LAB)
                img_open4 = cv2.imshow('Img Name', cvt_img_color3)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color3)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save8 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save8 == "Y" or img_save8 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC3.png', cvt_img_color3)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC3.png', cvt_img_color3)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC3.jpg', cvt_img_color3)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC3.jpg', cvt_img_color3)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save8 == "N" or img_save8 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!") exit()
            elif choose_color == "4" or choose_color == "RGB → XYZ":
                cvt_img_color4 = cv2.cvtColor(img_read4, cv2.COLOR_RGB2XYZ)
                img_open4 = cv2.imshow('Img Name', cvt_img_color4)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color4)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save9 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save9 == "Y" or img_save9 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC4.png', cvt_img_color4)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC4.png', cvt_img_color4)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC4.jpg', cvt_img_color4)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC4.jpg', cvt_img_color4)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save9 == "N" or img_save9 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
                    exit()
            elif choose_color == "5" or choose_color == "RGB → YCrCb":
                cvt_img_color5 = cv2.cvtColor(img_read4, cv2.COLOR_RGB2YCrCb)
                img_open4 = cv2.imshow('Img Name', cvt_img_color5)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color5)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save10 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save10 == "Y" or img_save10 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC5.png', cvt_img_color5)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC5.png', cvt_img_color5)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC5.jpg', cvt_img_color5)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC5.jpg', cvt_img_color5)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save10 == "N" or img_save10 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
                    exit()
            elif choose_color == "6" or choose_color == "LAB → RGB":
                cvt_img_color6 = cv2.cvtColor(img_read4, cv2.COLOR_Lab2LRGB)
                img_open4 = cv2.imshow('Img Name', cvt_img_color6)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color6)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save11 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save11 == "Y" or img_save11 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC6.png', cvt_img_color6)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC6.png', cvt_img_color6)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC6.jpg', cvt_img_color6)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC6.jpg', cvt_img_color6)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save11 == "N" or img_save11 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
                    exit()
            elif choose_color == "7" or choose_color == "XYZ → RGB":
                cvt_img_color7 = cv2.cvtColor(img_read4, cv2.COLOR_XYZ2RGB)
                img_open4 = cv2.imshow('Img Name', cvt_img_color7)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color7)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save12 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save12 == "Y" or img_save12 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC7.png', cvt_img_color7)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC7.png', cvt_img_color7)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC7.jpg', cvt_img_color7)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC7.jpg', cvt_img_color7)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save12 == "N" or img_save12 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            elif choose_color == "8" or choose_color == "YCrCb → RGB":
                cvt_img_color8 = cv2.cvtColor(img_read4, cv2.COLOR_YCrCb2RGB)
                img_open4 = cv2.imshow('Img Name', cvt_img_color8)

                try: img_open4 = cv2.imshow('Img Name', cvt_img_color8)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save13 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save13 == "Y" or img_save13 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC8.png', cvt_img_color8)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC8.png', cvt_img_color8)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name CIC8.jpg', cvt_img_color8)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name CIC8.jpg', cvt_img_color8)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save13 == "N" or img_save13 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            else:
                print("\033[1;31mPlease Check The Number Is Correct!")
        if choose_edit == "2" or choose_edit == "Add Effects":
            choose_effect = input("""\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mBlur
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mEdge Cascade
\033[1;37m[\033[1;33m3\033[1;37m]\033[1;33m - \033[1;37mDilated Effect
\033[1;37m[\033[1;33m4\033[1;37m]\033[1;33m - \033[1;37mEroded Effect
Choose \033[1;33m: \033[1;37m""")

            if choose_effect == "1" or choose_effect == "Blur":
                choose_blur = input("""\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mNormal Blur
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mGaussianBlur
\033[1;37m[\033[1;33m3\033[1;37m]\033[1;33m - \033[1;37mMedia Blurring
\033[1;37m[\033[1;33m4\033[1;37m]\033[1;33m - \033[1;37mBilateral Filtering
Choose \033[1;33m: \033[1;37m""")
                if choose_blur == "1" or choose_blur == "normal blur" or choose_blur == "Normal Blur":
                    num = int(input("Enter A Num Between 1-100 : "))
                    if num >= 1 and num <= 100:
                        blur_effect = cv2.blur(img_read4, (num, num))
                        img_open4 = cv2.imshow('Img Name', blur_effect)
                    else: print("Num Is Not Within Range!")

                    try: img_open4 = cv2.imshow('Img Name', blur_effect)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    img_save14 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                    if img_save14 == "Y" or img_save14 == "y":
                        choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                        if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)
 
                            cv2.imwrite('Img Name BI1.png', blur_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI1.png', blur_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)

                            cv2.imwrite('Img Name BI1.jpg', blur_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI1.jpg', blur_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        else: print("\033[1;31mPlease Check The Correct Option!")
                    elif img_save14 == "N" or img_save14 == "n":
                        print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                if choose_blur == "2" or choose_blur == "GaussianBlur" or choose_blur == "gaussianblur":
                    num = int(input("Enter A Num Odd Between 1-100 : "))
                    if num >= 1 and num <= 100: if num % 2 == 0: print("\033[1;31mPlease Enter An Odd Num")
                        gaussianblur_effect = cv2.GaussianBlur(img_read4, (num, num), 0)
                        img_open4 = cv2.imshow('Img Name', gaussianblur_effect)
                    else: print("Num Is Not Within Range!")

                    try: img_open4 = cv2.imshow('Img Name', gaussianblur_effect)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    img_save15 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                    if img_save15 == "Y" or img_save15 == "y":
                        choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                        if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)

                            cv2.imwrite('Img Name BI2.png', gaussianblur_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI2.png', gaussianblur_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)

                            cv2.imwrite('Img Name BI2.jpg', gaussianblur_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI2.jpg', gaussianblur_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        else: print("\033[1;31mPlease Check The Correct Option!")
                    elif img_save15 == "N" or img_save15 == "n":
                        print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                if choose_blur == "3" or choose_blur == "Media Blurring" or choose_blur == "media blurring":
                    num = int(input("Enter A Num Odd between 1-100 : "))
                    if num >= 1 and num <= 100: if num % 2 == 0: print("\033[1;31mPlease Enter An Odd Num")
                        media_blurring_effect = cv2.medianBlur(img_read4, num)
                        img_open4 = cv2.imshow('Img Name', media_blurring_effect)
                    else: print("Num Is Not Within Range!")

                    try: img_open4 = cv2.imshow('Img Name', media_blurring_effect)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    img_save16 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                    if img_save16 == "Y" or img_save16 == "y":
                        choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                        if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)

                            cv2.imwrite('Img Name BI3.png', media_blurring_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI3.png', media_blurring_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)

                            cv2.imwrite('Img Name BI3.jpg', media_blurring_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI3.jpg', media_blurring_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        else: print("\033[1;31mPlease Check The Correct Option!")
                    elif img_save16 == "N" or img_save16 == "n":
                        print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                if choose_blur == "4" or choose_blur == "BilateralFilter" or choose_blur == "bilateralfilter":
                    num = int(input("Enter A Num Between 1-100 : "))
                    if num >= 1 and num <= 100:
                        bilateralFilter_effect = cv2.bilateralFilter(img_read4, num, 75, 75)
                        img_open4 = cv2.imshow('Img Name', bilateralFilter_effect)
                    else: print("Num Is Not Within Range!")

                    try: img_open4 = cv2.imshow('Img Name', bilateralFilter_effect)
                    except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    img_save17 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                    if img_save17 == "Y" or img_save17 == "y":
                        choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                        if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)

                            cv2.imwrite('Img Name BI4.png', bilateralFilter_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI4.png', bilateralFilter_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                            directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                            os.chdir(directory_img)

                            cv2.imwrite('Img Name BI4.jpg', bilateralFilter_effect)
                            print("Successfully Saved!")

                            try: cv2.imwrite('Img Name BI4.jpg', bilateralFilter_effect)
                            except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                            exit()
                        else: print("\033[1;31mPlease Check The Correct Option!")
                    elif img_save17 == "N" or img_save17 == "n":
                        print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
            elif choose_effect == "2" or choose_effect == "Edge Cascade":
                t_lower = int(input("Enter The Lower Threshold Value : "))
                t_upper = int(input("Enter The Upper Threshold Value : "))
                aperture_size = int(input("Enter The Aperture Size Of The SobelFilter : "))

                edge_cascade = cv2.Canny(img_read4, t_lower, t_upper, aperture_size)

                img_open4 = cv2.imshow('Img Name - Edge Cascade Effect', edge_cascade)

                try: img_open4 = cv2.imshow('Img Name - Edge Cascade Effect', edge_cascade)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save18 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save18 == "Y" or img_save18 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name EC.png', edge_cascade)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name EC.png', edge_cascade)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite(filename, edge_cascade)
                        print("Successfully Saved!")

                        try: cv2.imwrite(filename, edge_cascade)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save18 == "N" or img_save18 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            elif choose_effect == "3" or choose_effect == "Dilated Effect":
                kernel_type = input("""\033[1;37mKernel Types
\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37mMORPH RECT
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37mMORPH ELLIPSE
\033[1;37m[\033[1;33m3\033[1;37m] \033[1;33m- \033[1;37mMORPH CROSS
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                if kernel_type == "1" or kernel_type == "MORPH RECT": kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
                elif kernel_type == "2" or kernel_type == "MORPH ELLIPSE": kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                elif kernel_type == "3" or kernel_type == "MORPH CROSS": kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
                else: print("\033[1;31mPlease Check The Correct Option!")
                iterations = int(input("\033[1;37mEnter The Num Of Iterations \033[1;33m: \033[1;37m"))
                dilated_effect = cv2.dilate(img_read4, kernel, iterations=iterations)

                img_open4 = cv2.imshow('Img Name - Dilated Effect', dilated_effect)

                try: img_open4 = cv2.imshow('Img Name - Dilated Effect', dilated_effect)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")  

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save19 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save19 == "Y" or img_save19 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name DE.png', dilated_effect)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name DE.png', dilated_effect)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite(filename, dilated_effect)
                        print("Successfully Saved!")

                        try: cv2.imwrite(filename, dilated_effect)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save19 == "N" or img_save19 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            elif choose_effect == "4" or choose_effect == "Eroded Effect":
                kernel_type = input("""\033[1;37mKernel Types
\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37mMORPH RECT
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37mMORPH ELLIPSE
\033[1;37m[\033[1;33m3\033[1;37m] \033[1;33m- \033[1;37mMORPH CROSS
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                if kernel_type == "1" or kernel_type == "MORPH RECT": kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
                elif kernel_type == "2" or kernel_type == "MORPH ELLIPSE": kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                elif kernel_type == "3" or kernel_type == "MORPH CROSS": kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
                else: print("\033[1;31mPlease Check The Correct Option!")
                iterations = int(input("\033[1;37mEnter The Num Of Iterations \033[1;33m: \033[1;37m"))
                eroded_effect = cv2.erode(img_read4, kernel, iterations=iterations)

                img_open4 = cv2.imshow('Img Name - Eroded Effect', eroded_effect)

                try: img_open4 = cv2.imshow('Img Name - Eroded Effect', eroded_effect)
                except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")  

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_save20 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
                if img_save20 == "Y" or img_save20 == "y":
                    choose_format = input("""\033[1;37m[\033[1;33m1\033[1;37m] \033[1;33m- \033[1;37m.png
\033[1;37m[\033[1;33m2\033[1;37m] \033[1;33m- \033[1;37m.jpg \033[1;37m
\033[1;37mChoose \033[1;33m: \033[1;37m""")
                    if choose_format == "1" or choose_format == ".png" or choose_format == ".PNG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite('Img Name EE.png', eroded_effect)
                        print("Successfully Saved!")

                        try: cv2.imwrite('Img Name EE.png', eroded_effect)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    elif choose_format == "2" or choose_format == ".jpg" or choose_format == ".JPG":
                        directory_img = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                        os.chdir(directory_img)

                        cv2.imwrite(filename, eroded_effect)
                        print("Successfully Saved!")

                        try: cv2.imwrite(filename, eroded_effect)
                        except Exception as error_opening_img: print(f"\033[1;31mPlease Check That The Img Name Or Path Is Correct!\n{error_opening_img}")            
                        exit()
                    else: print("\033[1;31mPlease Check The Correct Option!")
                elif img_save20 == "N" or img_save20 == "n":
                    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                    exit()
                else: print("\033[1;31mPlease Check The Correct Option!")
            else: print("\033[1;31mPlease Check The Correct Option!")
    if choose_option4 == "2" or choose_option4 == "Videos":
        vid_name3 = input("Enter The Vid Name Or Path \033[1;33m: \033[1;37m")
        vid_read3 = cv2.VideoCapture(vid_name3)

        choose_color = input("""Convert Colors
\033[1;37m[\033[1;33m1\033[1;37m]\033[1;33m - \033[1;37mRGB → Gray
\033[1;37m[\033[1;33m2\033[1;37m]\033[1;33m - \033[1;37mRGB → HSV
\033[1;37m[\033[1;33m3\033[1;37m]\033[1;33m - \033[1;37mRGB → LAB
\033[1;37m[\033[1;33m4\033[1;37m]\033[1;33m - \033[1;37mRGB → XYZ
\033[1;37m[\033[1;33m5\033[1;37m]\033[1;33m - \033[1;37mRGB → YCrCb
\033[1;37m[\033[1;33m6\033[1;37m]\033[1;33m - \033[1;37mLAB → RGB
\033[1;37m[\033[1;33m7\033[1;37m]\033[1;33m - \033[1;37mXYZ → RGB
\033[1;37m[\033[1;33m8\033[1;37m]\033[1;33m - \033[1;37mYCrCb → RGB
Choose \033[1;33m: \033[1;37m""")

        if choose_color == "1" or choose_color == "RGB → Gray":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color1 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                vid_open3 = cv2.imshow('Vid Name', cvt_vid_color1)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open3 = cv2.imshow('Vid Name', frame)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save3 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save3 == "Y" or vid_save3 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open3)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open3)
                except Exception as error_opening_vid:
                    print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save3 == "N" or vid_save3 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif choose_color == "2" or choose_color == "RGB → HSV":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color2 = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
                vid_open4 = cv2.imshow('Vid Name', cvt_vid_color2)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open4 = cv2.imshow('Vid Name', frame)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save4 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save4 == "Y" or vid_save4 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open4)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open4)
                except Exception as error_opening_vid:
                    print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")
                exit()
            elif vid_save4 == "N" or vid_save4 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif choose_color == "3" or choose_color == "RGB → LAB":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color3 = cv2.cvtColor(frame, cv2.COLOR_RGB2LAB)
                vid_open5 = cv2.imshow('Vid Name', cvt_vid_color3)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open5 = cv2.imshow('Vid Name', frame)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save5 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save5 == "Y" or vid_save5 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC3.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open5)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC3.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open5)
                except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save5 == "N" or vid_save5 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif choose_color == "4" or choose_color == "RGB → XYZ":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color4 = cv2.cvtColor(frame, cv2.COLOR_RGB2XYZ)
                vid_open7 = cv2.imshow('Vid Name', cvt_vid_color4)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open7 = cv2.imshow('Vid Name', frame)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save6 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save6 == "Y" or vid_save6 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC4.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open7)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC4.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open7)
                except Exception as error_opening_vid:
                    print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save6 == "N" or vid_save6 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif choose_color == "5" or choose_color == "RGB → YCrCb":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color5 = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)
                vid_open8 = cv2.imshow('Vid Name', cvt_vid_color5)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open8 = cv2.imshow('Vid Name', frame)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save7 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save7 == "Y" or vid_save7 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC5.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open8)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC5.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open8)
                except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save7 == "N" or vid_save7 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif choose_color == "6" or choose_color == "LAB → RGB":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color6 = cv2.cvtColor(frame, cv2.COLOR_Lab2LRGB)
                vid_open9 = cv2.imshow('Vid Name', cvt_vid_color6)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open9 = cv2.imshow('Vid Name', cvt_vid_color6)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save8 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save8 == "Y" or vid_save8 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC6.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open9)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC6.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open9)
                except Exception as error_opening_vid:
                    print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save8 == "N" or vid_save8 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif choose_color == "7" or choose_color == "XYZ → RGB":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color7 = cv2.cvtColor(frame, cv2.COLOR_XYZ2RGB)
                vid_open9 = cv2.imshow('Vid Name', cvt_vid_color7)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open9 = cv2.imshow('Vid Name', cvt_vid_color6)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save8 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save8 == "Y" or vid_save8 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC7.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open9)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC7.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open9)
                except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")            
                exit()
            elif vid_save8 == "N" or vid_save8 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        elif choose_color == "8" or choose_color == "YCrCb → RGB":
            while True:
                ret, frame = vid_read3.read()
                cvt_vid_color8 = cv2.cvtColor(frame, cv2.COLOR_YCrCb2RGB)
                vid_open9 = cv2.imshow('Vid Name', cvt_vid_color8)

                if cv2.waitKey(1) & 0xff == ord('q'): break
                    
            try: vid_open9 = cv2.imshow('Vid Name', cvt_vid_color8)
            except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path is Correct!\n{error_opening_vid}")

            vid_save8 = input("\033[1;37mDo You Want Save It? (\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
            if vid_save8 == "Y" or vid_save8 == "y":
                directory_vid = input("\033[1;37mEnter The Directory \033[1;33m: \033[1;37m")
                os.chdir(directory_vid)

                cv2.VideoWriter('Vid Name CVC8.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open9)
                print("Successfully Saved!")

                try: cv2.VideoWriter('Vid Name CVC8.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, vid_open9)
                except Exception as error_opening_vid: print(f"\033[1;31mPlease Check That The Vid Name Or Path Is Correct!\n{error_opening_vid}")
                exit()
            elif vid_save8 == "N" or vid_save8 == "n":
                print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")
                exit()
            else:
                print("\033[1;31mPlease Check The Correct Option!")
                exit()
        else: print("\033[1;31mPlease Check The Correct Option!")
else: print("\033[1;31mPlease Check The Correct Option!")
