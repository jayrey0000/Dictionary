def start_game():
    print("=== MAGING MAAGAP SA ESKWELA: ISANG TEXT-BASED NA LARO ===")
    print("Nagising ka ng alas-7:30 ng umaga! Malapit nang magsimula ang klase mo sa alas-8:00.")
    
    choice1 = input("Pupunta ka ba agad sa eskwelahan? (yes/no): ").lower()

    if choice1 == "yes":
        print("Lumabas ka ng bahay at nagmamadaling naglakad.")
        choice2 = input("Anong gagamitin mong transportasyon? (jeep/tricycle/lakad): ").lower()

        if choice2 == "jeep":
            print("Sumakay ka ng jeep pero may traffic!")
            choice3 = input("Bababa ka at maglalakad na lang? (yes/no): ").lower()

            if choice3 == "yes":
                print("Nagmamadali kang naglakad, pero pawisan ka pagdating sa eskwelahan.")
                choice4 = input("Pupunta ka muna sa CR para mag-ayos? (yes/no): ").lower()

                if choice4 == "yes":
                    print("Napatagal ka sa CR! Nahuli ka sa klase.")
                else:
                    print("Dumiretso ka sa classroom at umabot sa attendance!")

            else:
                print("Nagtiis ka sa traffic at nahuli sa klase.")

        elif choice2 == "tricycle":
            print("Mabilis kang nakarating pero kulang ang dala mong pera!")
            choice5 = input("Makikiusap ka ba sa driver na babayaran mamaya? (yes/no): ").lower()

            if choice5 == "yes":
                print("Pumayag ang driver at nakapasok ka sa eskwelahan!")
            else:
                print("Bumaba ka at naglakad na lang, pero huli ka sa klase.")

        elif choice2 == "lakad":
            print("Naglakad ka ng mabilis papunta sa eskwelahan.")
            choice6 = input("May nakita kang shortcut, dadaanan mo ba? (yes/no): ").lower()

            if choice6 == "yes":
                print("Napadali ang biyahe mo at umabot ka sa klase!")
            else:
                print("Dumaan ka sa normal na daan at sakto ka lang sa oras.")

    else:
        print("Nagtagal ka sa bahay at na-late sa klase.")
        choice7 = input("Pupunta ka pa rin ba sa eskwelahan? (yes/no): ").lower()

        if choice7 == "yes":
            print("Pumunta ka sa eskwelahan kahit late.")
            choice8 = input("Haharapin mo ba ang guro para magpaliwanag? (yes/no): ").lower()

            if choice8 == "yes":
                print("Pinaliwanag mo ang dahilan at pinayagan kang pumasok.")
            else:
                print("Pinili mong umuwi na lang sa bahay.")

        else:
            print("Nagdesisyon kang huwag pumasok ngayong araw.")

    print("=== SALAMAT SA PAGLALARO! ===")

start_game()