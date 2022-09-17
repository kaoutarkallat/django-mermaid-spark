import { trigger, state, style, transition, animate } from '@angular/animations';

export const Animations = {
    animeTrigger: trigger('inOut', [
        state('out', style({transform: 'scale(1)'})),
        state('in', style({transform: 'scale(1.1)'})),
        transition('in <=> out', animate('100ms'))
        // animate(700, keyframes([
        //     style({opacity: 0, transform: 'translateY(-100%)', offset: 0}),
        //     style({opacity: 1, transform: 'translateY(25px)',  offset: 0.3}),
        //     style({opacity: 1, transform: 'translateY(0)',     offset: 1.0}) 
        // ]))
    ]),
    animeTriggerText: trigger('inOutText', [
        state('out', style({})),
        state('in', style({backgroundColor:'rgba(40, 63, 95, 0.37)',color:'rgb(255, 255, 255)'})),
        transition('in <=> out', animate('100ms'))
    ]),
    itemFrameTr: trigger('inOutItemFrame', [
        state('out', style({})),
        state('in', style({
            // backgroundColor:'rgba(20, 20, 20, 0.77)',
            
        })),
        transition('in <=> out', animate('100ms'))
    ]),
    errorTrigger:trigger('error',[
        state('void',style({transform:"scale(0)",})),
        state('*',style({transform:"scale(1)",})),
        transition('*<=>void',[animate("300ms")])
    ]),
    zero2oneVTrigger:trigger('zero2oneV',[
        state('void',style({transform:"scale(0)",})),
        state('*',style({transform:"scale(1)",})),
        transition('*<=>void',[animate("300ms")])
    ]),
    menuTrigger:trigger('menu',[
        state('void',style({transform:"scale(0)",})),
        state('*',style({transform:"scale(1)",})),
        transition('*<=>void',[animate("1000ms")])
    ]),
    subRouteTrigger:trigger('subRoute',[
        state('void',style({opacity:0,})),
        state('*',style({opacity:1,})),
        transition('*=>void',[animate("5000ms")])
    ])

    

}