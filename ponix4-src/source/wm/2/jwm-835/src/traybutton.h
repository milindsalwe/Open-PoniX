/**
 * @file traybutton.h
 * @author Joe Wingbermuehle
 * @date 2004-2006
 *
 * @brief Button tray component.
 *
 */

#ifndef TRAY_BUTTON_H
#define TRAY_BUTTON_H

struct TrayComponentType;
struct TimeType;

/*@{*/
#define InitializeTrayButtons()  (void)(0)
void StartupTrayButtons();
#define ShutdownTrayButtons()    (void)(0)
void DestroyTrayButtons();
/*@}*/

/** Create a tray button component.
 * @param iconName The name of the icon to use for the button.
 * @param label The label to use for the button.
 * @param action The action to take when the button is clicked.
 * @param popup Text to display in a popup window.
 * @param width The width to use for the button (0 for default).
 * @param height The height to use for the button (0 for default).
 * @param border Set to show a border, 0 for no border.
 * @return A new tray button component.
 */
struct TrayComponentType *CreateTrayButton(const char *iconName,
                                           const char *label,
                                           const char *action,
                                           const char *popup,
                                           unsigned int width,
                                           unsigned int height,
                                           char border);

/** Validate the tray buttons and print a warning if something is wrong.
 * This is called after parsing the configuration file(s) to determine
 * if a root menu is defined for each each tray button that specifies
 * a root menu.
 */
void ValidateTrayButtons();

#endif /* TRAY_BUTTON_H */

